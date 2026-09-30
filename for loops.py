for x in range(100):
    x="Dorcas"

    print(x)







for letter in "Brian":
 print(letter)


for i in range(3):
   print("Hello")

for ch in "code":
   print(ch)

for n in range(10,0,-2):
   print(n)

for _ in range(3):
   print("Hello")



largest=0
for n in [4,9,2,7]:
   if n>largest:
      largest=n
print(largest)

#nested loop
for row in range(1,4):
    for col in range(1,4):
        print(row*col, end=" ")
    print()



for i in range(1,6):
   print("*" *i)





for i in range(1,6):
   print("*"*(6-i)) 



for i in range(1,6):
   print(""*(5-1)+"*"*i)



for i in range (1,6):
   for _ in range(i):
      print("*",end=" ")
   print()





for i in range(1,4):
   print("ab"*i)
for i in range(3):
   print("-" *i + "#")




for x in range(2,21):
   if x%2==0:
      print(x)


for x in range(2,21,2):
   print(x)


for x in range(1,20,3):
   print(x)

def is_leap_year(year):
   if year%400==0:
      return True
   elif year%100==0:
      return False
   elif year%4==0:
      return True
   else:
      return False
for year in range(1996, 2031):
    if is_leap_year(year):
        print(year)
