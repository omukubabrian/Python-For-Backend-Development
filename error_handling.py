try:
    n=int(input("Number: "))
    result =10/n
except ValueError:
    print("Not a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print(f"Result:{result:.2f}")
finally:
    print("Done.")