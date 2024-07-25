
class 클래스 이름 :

      <statement-1>

    ...

   <statement-n>


class Cat:
    def meow(self): #meow() 메소드 정의
        print("야옹")


cat1 = Cat() #인스턴스 생성

cat1.meow = Cat() #메소드 호출

class Cat:
    def meow(self):
        print("야옹")
    def sing(self): #두번째 메소드
        self.meow() #자기자신(self)의 메소드 호출
        print("미야옹")

cat1 = Cat()

cat1.sing()


class Cat:
    def info(self): #info() 메소드
        self.name = "블루" #인스턴스 변수 name 생성
        self.color = "회색" #인스턴스 변수 color
        print('고양이 이름은', self.name, '색깔은', self.color)


cat = Cat() #인스턴스 생성
cat.info() #인스턴스의 메소드 실행


class Cat:
    # 생성자 혹은 초기화 메소드라 한다.
    def __init__(self, name, color):
        self.name = name  # self.name 변수는 각각 cat1, cat2 인스턴스의 name을 가리킴
        self.color = color

        # 고양이 클래스의 정보를 출력하는 메소드

    def info(self):
        print('고양이 이름은', self.name, '색깔은', self.color)


cat1 = Cat("블루", "회색")  # cat1 인스턴스 생성
cat2 = Cat("미미", "갈색")  # cat2 인스턴스 생성

cat1.info()
cat2.info()