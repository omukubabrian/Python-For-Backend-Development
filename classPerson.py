class Person:
    def __init__(self,name):
        self.name=name

    def describe(self):
        raise NotImplementedError

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade

    def describe(self):
        return f"{self.name}, is a student in grade {self.grade}"


class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject

    def describe(self):
        return f"{self.name}, teaches {self.subject}"


people=[
    Student("Amina", 8),
    Teacher("Mr.Brian", "Math"),
    Student("Brian", 7),
    Student("Benita", 10),
    Teacher("Mr.Kamau", "Python"),
    Teacher("Saif", "Web Development")
]

for person in people:
    print(person.describe())
