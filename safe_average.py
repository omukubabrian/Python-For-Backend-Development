def safe_average(numbers):
    if len(numbers)>0:
        return sum(numbers)/len(numbers)
    else:
        return 0


print(safe_average([5,10,3]))
print(safe_average([]))
print(safe_average([0]))