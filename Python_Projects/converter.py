amount=float(input("Enter amount in USD: "))
rate=float(input("Enter exchange rate(e.g 129.5 for KES):"))
converted=amount*rate
print(f"{amount}USD={converted} KES")