class Dog:
    name = ""
    age = 0
    color = ""
    breed = ""

    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

    def run(self):
        print(self.name + ": 헥헥")

    def bark(self):
        print(self.name + ": 멍멍")

s = Dog("멈멈미", 10, "말티즈", "하얀색")
s.bark()


t = s
t.name = "댕댕이"
print(s.name)