items=[]
items.append(5)
items.append(10)
print(items)



numbers=[]
while True:
    num=int(input("Enter number (0 to stop):"))
    if num==0:
        break
    numbers.append(num)
print(f"Count:{len(numbers)}")
print(f"Total:{sum(numbers)}")


if len(numbers)>0:
    print(f"Max:{max(numbers)}")
    print(f"Min:{min(numbers)}")
    print(f"Average:{sum(numbers)/len(numbers)}")
else:
    print("No numbers entered")