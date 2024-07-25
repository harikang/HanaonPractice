import os
from helpers.debug import *


class Sec02_01:
    # 생파이썬
    # 배터리인클루디드 => 개발에 필요한 걸 가지고 나옴
    @staticmethod
    def Sec02_01_01():
        print(os.environ)

    @staticmethod
    def Sec02_01_02():
        print(os.getcwd())

    @staticmethod
    def Sec02_01_03():
        # pp(a)
        # a= "100"
        # pp(a)
        # a = int(a)
        # pp(dir("문자열"))
        #dir : 객체가 가지고 있는 속성 기능을 리스트 타입으로 리턴해줌
        #IDE => 통합개발환경
        #print(help(dir()))

        """
        내장함수 = 만들어져 있는거 쓰는 것
        :return:
        """
        pp("ggggggg")
        print(os.getcwd())

