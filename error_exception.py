try:
    age=int(input("Age: "))
except ValueError:
    print("Please enter a number")
else:
    print(f"Next year:{age + 1}")
finally:
    print("Done")