#함수를 클래스화를 함.
#괄호를 넣어서 object를 상속해도 좋으나 없기도 함.
#클래스 내부의 함수를 메소드라고 함.
#클래스를 바로 쓸 수도 있지만, 인스턴스화해서 써야함.
# __더블언더스코어__ : 던더

def doccheck(a):
    """
    :a: int
    :rtype: int
    """
    return a

class FirstChapter:
    """
    함수가 하는 일을 적어두는 곳
    """
    def __init__(self):
        pass
    def func(self): #클래스에 메서드를 정의할 때, self를 인자로 넣어주어야 함.
        return "chapter 1"
    #type hint , return하는 자료형이 동적자료형이라 고정은 안되지만 typehint로 할 수 있음.