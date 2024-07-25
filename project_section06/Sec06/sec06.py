#청사진, 설계도, 빵틀

class Robot:
    #생성자 :만들자마자 바로 정의되는 것을 init에 넣어줌.
    def __init__(self,name) -> None:
        #값
        self.color = "silver"
        #사전 정의하기 보다는 밖에서 받아오고 싶음. 
        self.name = name #->로봇을 만들때 이름정보를 필수적으로 받아와야함. 
        #init에는 return이 없어도 상관이 없음. 

    #기능
    def run(self,x):
        print(self.name,"는 앞으로", x**4,"m 달림.")
        #return을 하진 않았지만 자동으로 None이 return됨. 

class Myclass:
    pass

class Evil:
    def __new__(cls, *args):
        return 1
class MyClass2:
    def __init__(self, value):
        self.value = value

# @데코레이터
def 함수(a):
    return a 
#여기 쓰인 데코레이터는 함수 데코레이터 

#@데코레이터  -> 클래스 데코레이터는 여기 있을 것 같지만 
class 클래스명:
    # @데코레이터 #여기 쓰인 데코레이터가 클래스 데코레이터 
    def __init__(self) -> None:
        pass

def trace(func): #호출할 함수를 매개변수로 받음. 
    def wrapper():
        print(func.__name__,'함수 시작') # __name__으로 함수 이름 출력
        func()
        print(func.__name__,'함수 끝') 

    return wrapper #wrapper 함수 반환. 

