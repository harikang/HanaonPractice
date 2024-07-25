
# @데코레이터 : @어노테이션 인터프리터나 컴파일러한테 명시적으로 알려준다.
#데코레이터는 꾸며주는 함수라고 생각하면 편함

# 함수데코레이터
# 클래스데코레이터
#
# 파이썬: 미리 만들어둔 데코레이터
# 내가 만들어쓰는 사용자데코레이터
#
# 클래스데코레이터 : 클래스의 메소드를 꾸며준다
#
# @데코레이터
# def asdf(a):
#     return a
#
# class 클래스명:
#     @데코레이터
#     def ~
#
#         @property
#         @필드.setter
#         @staticmethod

##데코레이션 예제 (chatgpt)
# <데코레이션 없이 직접 직접적용>
# def my_decorator(func):
#     def wrapper():
#         print("함수 실행 전 무언가를 합니다..")
#         func()
#         print("함수 실행 후 무언가를 합니다.")
#     return wrapper
#
# def say_hello():
#     print("Hello!")
#
# say_hello = my_decorator(say_hello)
# say_hello()
#
# <데코레이션 사용>
# def my_decorator(func):
#     def wrapper():
#         print("함수 실행 전 무언가를 합니다..")
#         func()
#         print("함수 실행 후 무언가를 합니다.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()
#
# -------------------------------------------------

#접근제한자 , #데코레이션

#
# def trace(func):
#     def wrapper():
#         print(func.__name__,'함수 시작')
#         func()
#         print(func.__name__, '함수 끝')
#
#     return wrapper
#
# @trace
# def hello():
#     print('hello')
#
# hello()
# -----------------------------------------------------
#
# 속성(어트리뷰트): 값 밸류, 프라퍼티, 필드, 기능, (연관) 함수, 매소드(딘더메소드,사용자메소드)
#
# class Klass:
#     def __init__(self,x):
#         self.__x = x
#
#
#
# ------------------------------------------------------
#
# #스태틱 메서드 - 함수처럼 동작하는 메서드
#
# class Page:
#     def __init__(self, num, content):
#         self.num = num
#         self.content =content
#     @staticmethod
#     def check_blank(page):
#         return bool(page.content)
#
# page = page(1,'')
# page.check_blank(page)
#
# ----------------------------------------------------------
#
# # 추상클래스
# # 구체적인 구현은 안되어있음
# # 이름만 정의해뒀음
# # 값도 있고 기능도 있음
# #
# # 정의만 되어 있는게 한개라도 있으면 추상클래스라고 한다
# #
# # 구현을 상속받아서 쓰는 섭클래스에서 해야하면 인터페이스
#
# ##고양이 실습
# ##in cat.py
# class Cat:
#     def meow(self):
#         print("야옹")
#
#     def sing(self):
#         self.meow()
#         print("미야옹")
#
#     def info(self):
#         self.name = "블루"
#         self.color = "회색"
#         print('고양이 이름은', self.name, '색깔은', self.color)
#
#
# ##main.py
# from sec06.cat import Cat
# # for helpers.debug import *
#
# if __name__ == '__main__':
#     cat1 = Cat()
#     cat1.sing()
#
#     cat = Cat()  # 인스턴스 생성
#     cat.info()  # 인스턴스의 메소드 실행
#
# -----------------------------------------------------------------------------------------

# from pathlib import Path
# if __name__ =='__main__':
#     엑셀파일 = Path(r"C:\workspace\project01\07.22.txt")
#     텍스트파일.


-------------------

#파일 읽고 쓰기
# import pathlib
#
# # 읽기
# path = pathlib.Path('test.txt')
# file = path.read_text()
#
#
# # 쓰기
# path = pathlib.Path('test1.txt')
# path.write_text('파일쓰기')

#변수 value는 리스트 컴프리헨션으로 만들어진 스코프를 가지는 로컬 변수
# value for value in range(0)

# def f(x):
#     print(locals) #현재 로컬 스코프 내용을 표시
#     value='book'
#     print(locals())
#
# f('python')


































