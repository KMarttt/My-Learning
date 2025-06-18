class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, my name is {self.name}")



person1 = Person("Marti")
print(person1.name)
person1.talk()

