class Counter:
    def __init__(self)->None:
        self._value=0

    @property
    def value(self)->int:
        return self._value


    def increment(self)->None:
        self._value +=1

c=Counter()
print(c.value)

c.increment()
c.increment()
c.increment()
print(c.value)