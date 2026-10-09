class Employee:
    def __init__(self,name:str,base_salary:float)->None:
        self.name=name
        self.base_salary=base_salary

    def monthly_pay(self)->float:
        return self.base_salary

class Manager(Employee):
    def monthly_pay(self)->float:
        return self.base_salary * 1.20


people=[Employee("Alice",50000),
        Manager("Bob",80000),
        Employee("Carol",45000),
        Manager("Dave",90000)]

for person in people:
    print(f"{person.name}:{person.monthly_pay():.2f}")
