class Animal:
    def __init__(self):
        pass
    def speed(self,x):
        return x**5
    def size(self,y):
        return y**2
    
class Cat(Animal):
    def __init__(self,input):
        super(Cat,self).__init__()
        self.input = input
    def output(self):
        print(self.input)
    def weight(self,x):
        return x**3
    def sound(self):
        print("야옹")

class Dog(Animal):
    def __init__(self,input):
        super(Dog,self).__init__()
        self.input = input
    def output(self):
        print(self.input)
    def sound(self):
        print("멍멍")
