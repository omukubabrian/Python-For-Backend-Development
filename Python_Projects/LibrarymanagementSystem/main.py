from pathlib import Path
from library import Library

DATA_FILE = Path(__file__).parent.parent / "data" / "library.json"

MENU = """
=== Library ===
1. Add book
2. Add magazine
3. List all
4. List available
5. Search
6. Check out
7. Return
8. Quit"""


def show(items) -> None:
    if not items:
        print("Nothing found")
    for item in items:
        print(item)


def ask_id(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError:
        raise ValueError("ID must be a number.") from None


def main() -> None:
    library = Library(DATA_FILE)
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                print("Added:", library.add_book(title, author))
            elif choice == "2":
                title = input("Title: ")
                issue = input("Issue: ")
                print("Added:", library.add_magazine(title, issue))
            elif choice == "3":
                show(library.all_items())
            elif choice == "4":
                show(library.available())
            elif choice == "5":
                show(library.search(input("Search: ")))
            elif choice == "6":
                item_id = ask_id("Item ID: ")
                member = input("Member name: ")
                library.check_out(item_id, member)
                print("Checked out.")
            elif choice == "7":
                fee = library.return_item(ask_id("Item ID: "))
                print(f"Returned. Late fee: {fee:.2f}")
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice")
        except KeyError as error:
            print(f"Error: {error.args[0]}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()