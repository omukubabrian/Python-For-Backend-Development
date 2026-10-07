#JSON(Javascript Object Notation)is a text format for stractured data.It looks almost exactly like Pthon dictionaries and lists.



#saving bython dictionary
import json
student={"name":"Brian","age":21,"skills":["python","git"],"active":True}
with open("student.json","w") as f:
    json.dump(student, f ,indent=4)

#load file
with open("student.json","r") as f:
       data =json.load(f)
print(data["name"])
print(data["skills"][0])
print(type(data))