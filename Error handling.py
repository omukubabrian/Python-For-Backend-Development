#try:
 #  print(f"Next year you will be {age +1}")
#except ValueError:
 #   print("That was not anumber.")



try:
    result=10/int(input("Divide 10 by: "))
except ValueError:
    print("Type a whole number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
else:
    print(f"10 divided by that is {result}")



try:
    print("Step 1")
    print(10/0)
    print("Step 3")
except ZeroDivisionError:
    print("Problem handled")
print("Program continues")



ages={"Amina": 25,"Brian":30}
name=input("Name: ")
try:
    print(f"{name} is {ages[name]} years old")
except KeyError:
    print("Name not found")