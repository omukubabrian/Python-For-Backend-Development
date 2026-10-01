def safe_average(numbers):
    if len(numbers)>0:
        return sum(numbers)/len(numbers)
    else:
        return 0

numbers=[]
while True:
    num =int(input("Enter a number(0 to stop):"))
    if num==0:
        break
    numbers.append(num)

print(f"Count:{len(numbers)}")
print(f"Total:{sum(numbers)}")
print(f"Average:{safe_average(numbers)}")

if len(numbers)>0:
 print(f"Max:{max(numbers)}")
 print(f"Min:{min(numbers)}")