count =1
while count <=3:
    print(count)
    count=count+1



count=0
total=0
while True:
 num=int(input("Enter number(0 to stop):"))
 if num==0:
    break
 count+=num
 total+=num

print(f"Count: {count}")
print(f"Total: {total}")