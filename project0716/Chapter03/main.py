from project0716.Chapter03.part01 import *


if __name__ == "__main__":
    model = Chapter03
    #변수, 메모리
    model.part03() #괄호가 더해지면 함수를 호출하라는 의미
    print(model.part03) #괄호가 없으면 함수 자체를 의미하고 이를 print하면 이 메소드의 시작위치를 알 수 있음.
    print(id(model.part03)) #이 함수(인스턴스)가 할당받은 아이디를 알 수 있음.(파이썬이 작동되는 동안 고유한 값을 의미)


    #파이썬의 인터프리터가 타입을 유추해주기 때문임.
    #변수를 줄 때 type hint를 줄 수 있음.
    a : int = 4 #complie하기 전에 오류를 확인할 수 있기 때문에
    print(a)
    #파이썬은 알아서 동적타입으로 변환해준다. type casting

