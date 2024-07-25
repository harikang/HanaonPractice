# self를 통해 구체화된 인스턴스 자체를 참조
# this 암묵적으로, self 명시적으로

class Car:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def run(self):
        print("앞으로 달림")
