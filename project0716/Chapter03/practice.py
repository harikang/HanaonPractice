# #0부터 10까지 출력
# for i in range(11):
#     print(i)
#
# k=0
# while k<=10:
#     print(k)
#     k+=1
#
# for i in range(11):
#     if i%2 ==0:
#         print(i)

# k=0
# while k<=10 :
#     if k%2 ==0:
#         print(k)
#     k+=1

#구구단
# def gugudan(val):
#     print(f'{val}단 출력 시작')
#     for i in range(1,10):
#         print(val, "x", i ,"=", val*i)
#         # print("{} x {} = {} ".format(val,i,val*i))
#         print("%d %d %d")
# for k in range(2,3):
#     print('-'*10)
#     gugudan(k)
#     print('-' * 10)
import copy
items = [1,2]

#deep copy는 새로운 독립적인 object를 반환.
deep = copy.deepcopy(items)
#shallow copy는 주소와 id를 새롭게 생성하지만 값을 변경하면 같이 변화되어 독립적이지 않음.
shallow = items.copy() # 메모리 주소도 id도 찍어보면 둘이 서로 다름을 알 수 있음.

