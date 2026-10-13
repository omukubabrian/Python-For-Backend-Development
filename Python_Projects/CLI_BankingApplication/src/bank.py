"""Bank: users, accounts, rules and persistence."""

import json
from pathlib import Path

import auth
from accounts import ACCOUNT_TYPES, Account, account_from_dict, to_money


class AuthenticationError(Exception):
    """Raised for bad usernames and PINs."""


class AuthorizationError(Exception):
    """Raised when a user tries to touch an account that isn't theirs."""


class Bank:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._users: dict[str, dict] = {}
        self._accounts: dict[str, Account] = {}
        self.load()

    # ---- persistence ----
    def load(self) -> None:
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            users = raw["users"]
            accounts = {a["account_id"]: account_from_dict(a) for a in raw["accounts"]}
        except FileNotFoundError:
            return
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Warning: bank file is damaged. Starting empty.")
            return
        self._users = users
        self._accounts = accounts

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        raw = {
            "users": self._users,
            "accounts": [a.to_dict() for a in self._accounts.values()],
        }
        self.path.write_text(json.dumps(raw, indent=2), encoding="utf-8")

    # ---- users ----
    def register(self, username: str, pin: str) -> None:
        username = username.strip().lower()
        if not username.isalnum():
            raise ValueError("Username must be letters and numbers only.")
        if username in self._users:
            raise ValueError("That username is taken.")
        if not (pin.isascii() and pin.isdigit() and 4 <= len(pin) <= 6):
            raise ValueError("PIN must be 4 to 6 digits.")

        salt, digest = auth.hash_pin(pin)
        self._users[username] = {"salt": salt, "hash": digest}
        self.save()

    def login(self, username: str, pin: str) -> str:
        username = username.strip().lower()
        user = self._users.get(username)

        if user is None:
            auth.hash_pin(pin)   # same time spent, so speed can't reveal valid usernames
            raise AuthenticationError("Invalid username or PIN.")
        # Same message for both failures so attackers can't discover valid usernames.
        if not auth.verify_pin(pin, user["salt"], user["hash"]):
            raise AuthenticationError("Invalid username or PIN.")
        return username

    # ---- accounts ----
    def open_account(self, owner: str, kind: str, initial_deposit: object = "0") -> Account:
        if kind not in ACCOUNT_TYPES:
            raise ValueError("Account type must be 'checking' or 'savings'.")
        amount = to_money(initial_deposit)
        if amount < 0:
            raise ValueError("Opening deposit cannot be negative.")

        account_id = f"ACC-{len(self._accounts) + 1:04d}"
        account = ACCOUNT_TYPES[kind](account_id, owner)
        if amount > 0:
            account.deposit(amount, note="opening deposit")
        self._accounts[account_id] = account
        self.save()
        return account

    def accounts_of(self, owner: str) -> list[Account]:
        return [a for a in self._accounts.values() if a.owner == owner]

    def get_account(self, owner: str, account_id: str) -> Account:
        """Authorization check: only the owner may access the account."""
        account = self._accounts.get(account_id.strip().upper())
        if account is None or account.owner != owner:
            raise AuthorizationError("Account not found.")
        return account

    def deposit(self, owner: str, account_id: str, amount: object) -> None:
        self.get_account(owner, account_id).deposit(amount)
        self.save()

    def withdraw(self, owner: str, account_id: str, amount: object) -> None:
        self.get_account(owner, account_id).withdraw(amount)
        self.save()

    def transfer(self, owner: str, from_id: str, to_id: str, amount: object) -> None:
        source = self.get_account(owner, from_id)
        target = self._accounts.get(to_id.strip().upper())
        if target is None:
            raise ValueError("Destination account not found.")
        if target is source:
            raise ValueError("Cannot transfer to the same account.")

        amount = to_money(amount)
        source.withdraw(amount, note=f"transfer to {target.account_id}")
        target.deposit(amount, note=f"transfer from {source.account_id}")
        self.save()