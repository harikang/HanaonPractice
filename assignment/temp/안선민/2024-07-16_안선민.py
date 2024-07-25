# fruit = ["apple", "key"]
#
# for i in fruit:
#     print(f'과일이름은 {fruit} 입니다.')
#     #print (f'{}번째 과일은 {fruit} 입니다.)
#
# for i in range(0,len(fruit)):
#     print(f'과일이름은 {fruit}입니다.')
#     print(f'{i}번째 과일은 {fruit}입니다.')
#
# for idx, i in enumerate(fruit):
#     print(f'과일이름은 {i} 입니다.')
#     print(f'{idx}번째 과일은 {fruit} 입니다')
#
#
# chars = 'word'
# for count, char in enumerate(chars):
#     print(f'{count}번째 문자는 {char}')


# print(m)

# for m in range(3):
#     x=10
#     print(m)
# print(x)


# n=0
# while n<3:
#     print(f'변수 n의 값은 {n}')
#     n +=1


##0부터 100까지 for/while문으로 출력해보기
# for i in range(0,101):
#     print(i)
#     i +=1
#
# n = 0
# while n<101:
#     print(n)
#     n +=1
#
#
# ##짝수만 출력
# for i in range(0,101):
#     if i %2 == 0:
#         print(i)
#     i +=1
#
# n=0
# while n<101:
#     if n %2 ==0:
#         print(n)
#     n +=1

##구구단 출력
# for i in range(2,10):
#     for k in range(1,10):
#         print(i*k)
#
# n=2
# while n <=9:
#     num=1
#     while num <10:
#         print(f'{n}*{num}은 {n*num}입니다.')
#         num += 1
#     n +=1

# for i in range(0,8):
#     print("===="+f'{i+2}단'+"====")
    # print("=".center(10))
    # for j in range(0,9):
        # print(f"{i+2} * {j+1} = {(i+2)*(j+1)}")
        # print("{} * {} * {}".format(i+2,j+1,(i+2)*(j+1)))
        # print("{} * {} {0:>2}".format((i+2)*(j+1)))

# def has_book(items):
#
#     items =[1,2]
#
#     item.pop()
#     copied = items.copy()
#     #원본에 값을 직접 가지고 있는지, 메모리주소만 참조
#
#     while copied:
#         item=copied.pop()
#         if 'book' in item:
#             print('Found')
#             break
#     else:

# import random
# def lottery(goods):
#     if item := random.choice(goods):
#         return item
#     else:
#         return 'MISS!'
#

# try :
#     import asdfsafsdfsafs
# except Exception as e:
#     print(e)
# finally:
#     #예외랑 상관없이 할일부분을 적어주면됨
#     print(e)


# items =[1,2,3]
#
# i=10
# try:
#     items[i]
# except Exception as e:
#     print(e)
#     i -=1


# from io import UnsupportedOperation
# f= open('some.txt','w')
# try:
#     f.read()
# except UnsupportedOperation as e:
#     print(f'예외가 발생했습니다:{e}')
# finally:
#     print('파일을 닫습니다')
#     f.close()

#
# with open('some.txt','w') as f:
#     print(f.read)
#     print(f.readline)
#     print(f.readlines)
#
#     f.write('some text')


# str(print('book'))
#
# def asdf():
#     print()
#
# d = {'a':1,"b":2}
# d["c"]
# d.get('c')








