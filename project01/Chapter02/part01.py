import os  # 내장 모듈(py파일)
from project01.helpers.debug import *


class Part01:
    def __init__(self):
        pass
        # PATH : os에 경로를 알려줌.
        # battery included : 배터리가 들어있다는 뜻. 파이썬은 개발 시 필요한 것들을 가지고 있는 언어라는 뜻.
        # 운영 체제 관련이 모두 들어있음.
        # 바로 쓰는 메소드 데코레이터(@)

    @staticmethod
    def subpart1():
        print(os.environ)  # 이 자체가 값.

    @staticmethod
    def subpart2():
        print(os.getcwd())
        # pwd를 알려줌, get current working directory

    @staticmethod
    def subpart3():
        # 내장함수 : builtin function, 내가 정의하지 않은 사전에 정의된 함수 e.g.print()
        # type() # type을 알려주는 클래스의 초기함수를 받아들여서 return하기에 함수로 여겨지기도 함.
        # print() # 출력해주는 overload method임.
        pp("잘됨")
        #원시타입, primitive type
        # -> int, float, bool, str
        #원시타입은 type casting

    def subpart4():
        a = "100"
        pp(a)
        a = int(a)
        pp(a)
        pp(dir("문자열"))
        #dir : 객체가 가지고 있는 속성, 기능을 list type으로 return해준다.
        # IDE : Integrated Development Enviornment
        #"문자열". 사전에 정의된 함수들이 많음. (len, getitem, doc, eq, 등등)
        print(help(dir()))