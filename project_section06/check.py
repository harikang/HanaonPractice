# items = {'note': 1, 'notebook': 2, 'sketchbook': 3}
#
# for i in items.keys():  # 키만 얻음
#     print(i)
#
# for key in items:
#     print(key)

# list = []
#
# for i in range(101):
#     if i%2 ==0:
#         list.append(i)
#
# compressed_list = [i for i in range(101) if i%2 ==0] #list에 써야하는 값을 앞에 넣음.
#
# print(list)
# print(compressed_list)
# print("구구단")
# gugudan = [f"{i} x {j} = {i*j}" for i in range(1,10) for j in range(1,10) if i % 2 ==0]
# print(gugudan)

#generator

# from datetime import datetime
# d = datetime.now() #인스턴스화 없이 쓸 수 있는 static method
# #변수 선언하고 호출하면서 사용해야함.
# #호출될때마다 시간이 바뀌기 때문에 정의부에 담아둘 수 없음.
# print(d)

increment = lambda num: num+1 # lambda 식으로 함수를 정의함.
# #lambda input : output
nums = [1,2,3,4,5]
# filtered = filter(lambda x : len(x) ==3, nums)
# print(list(filtered)) #list화해주면 출력이 됨.

# def lenthree(val):
#     if len(val)==3:
#         return True
#     else:
#         return False
#
# filtered = filter(lenthree,nums)
# print(list(filtered))

# def multiplication(a):
#     return a*2
#
# mapped = map(lambda a : 2*a,nums)
# print(list(mapped))
#
# mapped2 = map(multiplication,nums)
# print(list(mapped2))
#
# from functools import reduce
# reduce(lambda x, y: x+y, [1,2,3,4,5])

# def decrement(page_num: int) -> int:
#     prev_page: int  # 타입 정보를 붙여 변수를 선언함
#     prev_page = page_num - 1
#     return prev_page
#
# # 실행 시 타입 체크는 하지 않으므로 에러는 발생하지 않음
# print(decrement(2.0))

# def asdf(a,b,c)->str:
#     """_summary_
#
#     Args:
#         a (int): nominator
#         b (int): denominator
#         c (boolean): True, False
#     """
#
#     return "happy"
#
#
# print(asdf.__doc__)

