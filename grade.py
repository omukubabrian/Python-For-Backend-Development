score=int  (input("Enter Exam Score: "))
if score < 0 or score > 100:
       print("Invalid score!")
elif score >= 80:
       print("A")
elif score >= 70:
       print("B")
elif score >=60:
       print("C")
else:
       print("F")