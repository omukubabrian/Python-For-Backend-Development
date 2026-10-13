"""Account models with encapsulated balances"""
from datetime import datetime
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

CENT = Decimal("0.01")


class InsufficientFundsError(Exception):
    """Raised when an account cannot cover a withdrawal."""


def to_money(value: object) -> Decimal:
    """Convert input to a 2-decimal Decimal or raise ValueError."""
    try:
        amount = Decimal(str(value).strip())
        if not amount.is_finite():
            raise ValueError("Invalid amount.")
        return amount.quantize(CENT, rounding=ROUND_HALF_UP)
    except InvalidOperation:
        raise ValueError("Invalid amount.") from None


class Account:
    kind = "account"

    def __init__(self, account_id: str, owner: str,
                 balance: object = "0.00",
                 history: list[dict] | None = None) -> None:
        self.account_id = account_id
        self.owner = owner
        self._balance = to_money(balance)
        self._history: list[dict] = list(history) if history else []

    @property
    def balance(self) -> Decimal:
        return self._balance

    @property
    def history(self) -> list[dict]:
        return list(self._history)

    def _record(self, kind: str, amount: Decimal) -> None:
        self._history.append({
            "time": datetime.now().isoformat(timespec="seconds"),
            "type": kind,
            "amount": str(amount),
            "balance_after": str(self._balance),
        })

    def _can_withdraw(self, amount: Decimal) -> bool:
        return amount <= self._balance

    def deposit(self, amount: object, note: str = "deposit") -> None:
        amount = to_money(amount)
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero.")
        self._balance += amount
        self._record(note, amount)

    def withdraw(self, amount: object, note: str = "withdrawal") -> None:
        amount = to_money(amount)
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero.")
        if not self._can_withdraw(amount):
            raise InsufficientFundsError("Insufficient funds.")
        self._balance -= amount
        self._record(note, amount)

    def to_dict(self) -> dict:
        return {
            "kind": self.kind,
            "account_id": self.account_id,
            "owner": self.owner,
            "balance": str(self._balance),
            "history": self.history,
        }


class CheckingAccount(Account):
    kind = "checking"
    overdraft_limit = Decimal("100.00")

    def _can_withdraw(self, amount: Decimal) -> bool:
        return amount <= self._balance + self.overdraft_limit


class SavingsAccount(Account):
    kind = "savings"
    interest_rate = Decimal("0.02")

    def add_interest(self) -> Decimal:
        interest = (self._balance * self.interest_rate).quantize(
            CENT, rounding=ROUND_HALF_UP)
        if interest > 0:
            self.deposit(interest, note="interest")
        return interest


ACCOUNT_TYPES = {"checking": CheckingAccount, "savings": SavingsAccount}


def account_from_dict(data: dict) -> Account:
    cls = ACCOUNT_TYPES[data["kind"]]
    return cls(data["account_id"], data["owner"], data["balance"], data["history"])