import os
from helpers.debug import *


class Sec02_01:
    # 생파이썬
    # 배터리 인클루디드
    @staticmethod
    def Sec02_01_01():
        print(os.environ)

    @staticmethod
    def Sec02_01_02():
        print(os.getcwd())

    @staticmethod
    def Sec02_01_03():
        """
        내장함수 빌트인펑션
        내가정의하진 않았어
        미리다 만들어놓았음
        타입을 확인해준다
        """
        pp("잘됨")
        print(os.getcwd())

        # 원시타입 프리미티브타입스  레퍼런스타입
        # int
        # float
        # bool
        # str
        # 원시타입은 타입캐스팅
        #
        # 파이썬은
        # 동적타입 암묵적(묵시적)변환 영어로 타입캐스팅
        # 명시적변환 개발자가              타입컨버전

        # 하이픈 -V
        # 통용되는규칙
        # --풀네임 --version
        # -축약 -v

        a = "100"
        pp(a)
        a = int(a)
        pp(a)
        pp(dir("문자열"))
        # dir : 객체가 가지고 있는 속성 기능을 리스트 타입으로 리턴해준다
        print(help(dir()))