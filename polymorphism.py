#Different objects respond to the same method call in their own way
animals=[Dog("Rex","lab"),Animal("Generic")]
for animal in animals:
    print(animal.speak())