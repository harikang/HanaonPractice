class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Meow!"


cat1 = Cat("Nabi", "White")
print(cat1.speak())
print(cat1.name)
print(cat1.color)