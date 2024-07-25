#예외처리
#exception
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
from io import UnsupportedOperation
import os
os.getcwd()
f = open(r'D:\workspace_hanabank\project0716/0716.txt','w') #file을 읽기모드로 열지 쓰기 모드로 열지를 결정 'w','a','r'
#mode ="" -> keyword인자로 나타나게 됨.
try :
    import alkdafjadfj
except Exception as e:
    #예외 전부를 받을 때, Exception으로 받음.
    print(e)
finally : #예외랑 상관없이 할 일
    print("예외랑 무관하게 출력됨.")


