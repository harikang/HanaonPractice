from animals import *

if __name__ =="__main__":
    dog = Dog(2)
    dog.output() #1
    print(dog.speed(5)) #2
    
    cat = Cat(4)
    cat.sound() #3
    print(cat.size(4)) #4

    # output = model(data)은 model.forward(data)와 동일함.