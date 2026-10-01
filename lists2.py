numbers=[6,34,67,23]
if len(numbers)>0:
 print(f"Count:{len(numbers)}")
 print(f"Total:{sum(numbers)}")
 print(f"Max:{max(numbers)}")
 print(f"Min:{min(numbers)}")
 print(f"Average:{sum(numbers)/len(numbers):.2f}")
else:
 print("No  numbers entered")