from sec06 import *
from book import *
from inherit import *

if __name__ == "__main__":
    # #클래스를 이용하여 인스턴스화함. one과 two에 담김. 
    # one = Robot("1호")
    # two = Robot("2호")
    # print(one.color, type(one.color)) #생성자에 미리 선언해둔 변수.    
    # one.run(15)
    # two.run(18)
    # one.color = "red"
    # print(one.color, type(one.color)) #instance에 직접 접근해서 값을 수정. main에서 변화시키면? -> 반영됨. 함수가 수정됨. 
    # #robot1의 새로운 method를 통해서 값을 수정하도록하여 함수 안에 논리를 추가하여 검증을 할 수 있도록 바꿈. = setter를 만들어줌. 

    # # 그냥 object 상속한 형태로 아무것도 안선언.
    # test = Myclass()
    # print(isinstance(test,Myclass)) #True

    # # new만 사용
    # evil = Evil()
    # print(isinstance(evil, Evil)) #False

    # instance = MyClass2(2)
    # # init만 사용
    # print(isinstance(instance, MyClass2))  # True

    # @trace
    # def hello():
    #     print("decorater 내부 함수가 호출됨.")
    
    # hello()

    # book = Book(30000)
    # print(book.discounts)
    # print(book.price)

    # book.discounts = 20  # 할인율 설정

    # print(book.discounts)
    # print(book.price)
    
    # rawbook = rawBook(50000)
    # print(rawbook.raw_price)
    # print(rawbook.discount())
    # print(rawbook.price())
    # rawbook.discounts(50)
    # print(rawbook.price())

    # klsl = Klass()   
    # kls2 = Klass()   
    # # 클래스 변수 업데이트하면 모든 인스턴스의 변수가 함께 업데이트됨. 
    # klsl._x = 3    
    # print(klsl._x)
    # print(klsl.book_title)
    # print(kls2.book_title)
    # Klass.book_title = 'Python Practice Book update'
    # print(klsl.book_title)
    # print(kls2.book_title)

    # first = Page(1, 'first page')
    # second = Page(2, 'second page')
    # third = Page(3, 'third page')

    # # 클래스 메서드 호출
    # Page.print_pages(first, third, second)

    # # 인스턴스에서도 호출할 수 있음
    # third.print_pages(first, third, second)

    # page = Page(1, '')
    #인스턴스를 선언하지 않아도 클래스만 import해오면 바로 사용할 수 있는 method
    # print(Page.addition(1,2))
    
    d = D()
    d.hello()

    print(D.__mro__)  # 메서드 결정 순서 확인