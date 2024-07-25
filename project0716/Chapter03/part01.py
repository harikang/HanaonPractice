import sys
import os
from project01.Chapter02.part01 import *
from project01.helpers.debug import *

class Chapter03:
    def part01():
        #들여쓰기는 스페이스바 4칸
        #들여쓰기를 안해주면 syntex error가 발생함.
        #버전 표기법
        major = sys.version_info.major
        minor = sys.version_info.minor
        pp(major)
        print()
        pp(minor)
        pass
        ... #elipses, pass를 ...으로 대체할 수 있음.

    def part02():
        #지금은 메서드를 정의할 수 없고
        #일단 선언만 할게라는 의미로 pass를 하면 됨.
        pass

    def part03():
        print("hello world")