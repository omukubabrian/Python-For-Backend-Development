from pathlib import Path
from library import Library

DATA_FILE=Path(__file__).parent.parent/"data"/"library.json"


#MENU
#===Library===
#1.Add book
#2.Add magazine
#3.List all
#4.List available
#5.search
#6.Check out
#7.Return
#8.Quit"""


def show(items)->None:
    if not items:
        print("Nothing found")
    for item in items:
        print(item)



def ask_id(propmt:str)->int:
    try:

        return int(input(prompt))
    except ValueError:
        raise ValueError("ID must be a number.")from None

def main()->None:

    library=Library(DATA_FILE)
    while True:
        print(MENU)
        choice=input("Choose:").strip()
        try:
            if choice=="1":
                print("Added:",library.add_book(input("Title:"),input("Author")))
            elif choice=="2":
                print("Added",library.add_magazine(input("Title:"),input("Issue:")))

            elif choice=="3":
                show(library.all_items())
            elif choice=="4":
                show(library.available())
            elif choice=="6":
                library.check_out(ask_id("Item ID: "),input("Member name: "))
                print("Check out")


            elif choice=="7":
                fee=library.return_items(ask_id("Item ID:"))
                print(f"Returned.Late fee:{fee:.2f}")
            elif choice=="8":
                break

            else:
                print("Invalid choice")

        except(ValueError,KeyError)as error:
            print(f"Error:{error}")


        if __name__=="__main__":
            main()