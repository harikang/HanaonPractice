class A:
    def hello(self):
        print('Hello')
        # print('a',super())

class C(A):
    def hello(self):
        print('안녕하세요')
        # print('c',super())
        super().hello()  # 베이스 클래스의 메서드를 실행
        # print('c2',super())

class B(A):    
    def hello(self):
        print('Hola')
        # print('b',super())
        super(B, self).hello()
        # super().hello()  # 베이스 클래스의 메서드를 실행
        # print('b2',super())



class D(C,B):
    def hello(self):
        print('Xin Chao')
        # print('d',super())
        super().hello()  # 베이스 클래스의 메서드를 실행
        # print('d2',super())