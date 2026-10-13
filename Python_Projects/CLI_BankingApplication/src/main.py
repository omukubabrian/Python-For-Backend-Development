"""Banking command line interface."""
from pathlib import Path

from accounts import InsufficientFundsError, SavingsAccount
from bank import AuthenticationError, AuthorizationError, Bank

DATA_FILE = Path(__file__).parent.parent / "data" / "bank.json"
MAX_ATTEMPTS = 3
ERRORS = (ValueError, InsufficientFundsError, AuthorizationError)


def account_menu(bank: Bank, user: str) -> None:
    while True:
        print(f"\n--- {user} ---")
        print("1. Open account   2. My accounts   3. Deposit   4. Withdraw")
        print("5. Transfer   6. History   7. Add interest (savings)   8. Log out")
        choice = input("Choice: ").strip()

        try:
            if choice == "1":
                kind = input("Type (checking/savings): ").strip().lower()
                account = bank.open_account(user, kind, input("Initial deposit: "))
                print(f"Opened {account.account_id}")

            elif choice == "2":
                accounts = bank.accounts_of(user)
                if not accounts:
                    print("You have no accounts yet.")
                for a in accounts:
                    print(f"{a.account_id}  {a.kind:<9} {a.balance:>10}")

            elif choice == "3":
                bank.deposit(user, input("Account ID: "), input("Amount: "))
                print("Deposited.")

            elif choice == "4":
                bank.withdraw(user, input("Account ID: "), input("Amount: "))
                print("Withdrawn.")

            elif choice == "5":
                bank.transfer(user, input("From: "), input("To: "), input("Amount: "))
                print("Transferred.")

            elif choice == "6":
                for t in bank.get_account(user, input("Account ID: ")).history:
                    print(f"{t['time']} {t['type']:<22} {t['amount']:>10} bal {t['balance_after']}")

            elif choice == "7":
                account = bank.get_account(user, input("Account ID: "))
                if isinstance(account, SavingsAccount):
                    print(f"Interest added: {account.add_interest()}")
                    bank.save()
                else:
                    print("Only savings accounts earn interest.")

            elif choice == "8":
                return

            else:
                print("Invalid choice.")

        except ERRORS as error:
            print(f"Error: {error}")


def main() -> None:
    bank = Bank(DATA_FILE)
    failures = 0
    while True:
        print("\n=== PyBank ===")
        print("1. Register   2. Log in   3. Quit")
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                bank.register(input("Username: "), input("PIN (4-6 digits): "))
                print("Registered. You can log in now.")

            elif choice == "2":
                if failures >= MAX_ATTEMPTS:
                    print("Too many failed attempts. Restart the program.")
                    continue
                try:
                    user = bank.login(input("Username: "), input("PIN: "))
                except AuthenticationError as error:
                    failures += 1
                    print(f"Error: {error} ({MAX_ATTEMPTS - failures} attempts left)")
                    continue
                failures = 0
                account_menu(bank, user)

            elif choice == "3":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()