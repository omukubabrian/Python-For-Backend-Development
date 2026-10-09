class Animal:
    def __init__(self,name:str)->None:
        self.name=name

    def speak(self)->str:
        return"..."

class Dog(Animal):
    def __init__(self,name:str,breed:str)->None:
        super().__init__(name)
        self.breed=breed

    def speak(self)->str:
        return "Woof!"