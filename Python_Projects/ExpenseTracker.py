def save_expenses(expenses):
    with open("expenses.txt","w") as f:
        for amount in expenses:
            f.write(f"{amount}\n")

def load_expenses():
    expenses =[]
    try:
        with open("expenses.txt","r") as f:
            for line in f:
                expenses.append(int(line.strip()))

    except FileNotFoundError:
        pass
    return expenses

expenses = load_expenses()
while True:
    text=input("Enter expense(or 'q' to quit): ")
    if text=="q":
        break
    try:
        expenses.append(int(text))
    except ValueError:
        print("Please type a number.")

save_expenses(expenses)
print(f"Count:{len(expenses)}")
print(f"Total:{sum(expenses)}")
print(f"Biggest three:{sorted(expenses, reverse=True)[:3]}")