# 속성을 이용한 정렬에 사용할 수 있는 표준 라이브러리를 임포트
from operator import attrgetter

class Book: 
    def __init__(self, raw_price): #book이라는 class를 통해서 책이라는 인스턴스가 생기면 생기는 것
        if raw_price < 0:
            raise ValueError('price must be positive')
        self.raw_price = raw_price #인자와 변수를 동일하게 받아들임.
        self._discounts = 0 
    @property #인스턴스 변수(값)을 메소드를 통해서 접근하고 다룸 / getter
    def discounts(self):
        return self._discounts
    @discounts.setter # 인스턴스 변수(값)을 메소드를 통해서 선언 / setter 
    def discounts(self, value):
        if value < 0 or 100 < value:
            raise ValueError(
                'discounts must be between 0 and 100')
        self._discounts = value
    @property #인스턴스 변수(값)을 메소드를 통해서 접근하고 다룸 / getter
    def price(self):
        multi = 100 - self._discounts
        return int(self.raw_price * multi / 100)
    
class rawBook: 
    def __init__(self, raw_price): #book이라는 class를 통해서 책이라는 인스턴스가 생기면 생기는 것
        if raw_price < 0:
            raise ValueError('price must be positive')
        self.raw_price = raw_price #인자와 변수를 동일하게 받아들임.
        self._discounts = 0 
    #@property #인스턴스 변수(값)을 메소드를 통해서 접근하고 다룸 / getter
    def discount(self):
        return self._discounts
    #@discounts.setter # 인스턴스 변수(값)을 메소드를 통해서 선언 / setter 
    def discounts(self, value):
        if value < 0 or 100 < value:
            raise ValueError(
                'discounts must be between 0 and 100')
        self._discounts = value
    #@property #인스턴스 변수(값)을 메소드를 통해서 접근하고 다룸 / getter
    def price(self):
        multi = 100 - self._discounts
        return int(self.raw_price * multi / 100)
    

class Klass:
    book_title = 'Python Practice Book' # self가 없는 변수 
    def __init__(self):
        self.__x = 300 #underscore 2개면 참조가 안되어 출력이 안됨. 
        self._x = 3000
    
class Page:
    book_title = 'Python Practice Book'
    cnt =0
    def __init__(self, num, content):
        self.num = num
        self.content = content
    def output(self):
        return f'{self.content}'
    # 클래스 메서드의 첫 번째 인수는 클래스 객체
    @classmethod
    def print_pages(cls, *pages): #instance를 가르키는 것이 아니라 class 전체를 가르키는 것이기 때문에 cls로 붙임. # *은 가변 위치 인자(list)
        # 클래스 객체 이용
        print(cls.book_title)
        cls.cnt +=1
        print(cls.cnt)
        pages = list(pages)
        # 페이지 순으로 정렬해서 출력
        for page in sorted(pages, key=attrgetter('num')):
            print(page.output())

    @staticmethod  # 스태틱 메서드로 정의
    def check_blank(page):
        return bool(page.content)
    
    # # 이 메서드는 인스턴스가 선언되어야 사용할 수 있는 메소드 
    # def addition(self,a,b):
    #     return a+b
    
    # 이 메서드는 클래스만 정의해주면 사용할 수 있는 메소드 
    @staticmethod
    def addition(a,b):
        return a+b