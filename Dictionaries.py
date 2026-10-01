student={"Name":"Brian","age": 25 ,"city": "Nairobi"}
print(f"{student['Name']} is {student['age']} years old and lives in {student['city']}")
print(student.get("phone","not given"))
print("age" in student)
student["age"]=26
student["phone"]="0712453988"
print(student)