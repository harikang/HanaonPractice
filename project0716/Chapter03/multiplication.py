items = [1,2,3]
# for i in items:
#     print(f'변수 i의 값은 {i}')

fruits = ["apple","pear","banana","grapes"]

# for val in fruits:
#     print(f'과일이름은 {val}입니다.')
#
# for i in range(len(fruits)):
#     print(f'과일이름은 {fruits[i]}입니다.')
#
# for i , val in enumerate(fruits):
#     print(f'{i+1}번쨰 과일이름은 {val}입니다.')

# for i in range(0,10,3):
#     print(i,"출력")
# nums = [11,12,13,14]
# even = [2,4,6,8]
# odd = [1,3,5,7,9]
# for val in nums:
#     if val % 2 ==0 : #짝수면
#         even.append(val)
#     elif val % 2 ==1 : #혹수면
#         odd.extend([val])
# print(even, odd)

i=0
def repeats(val):
    global i
    for i in range(val):
        print(i)

repeats(3)
print(i)
