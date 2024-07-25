def 성적처리():
    ###
    return 결과

if
elif
else
출력

성적을 입력하세요 print()

def 성적처리(점수):
    if 점수 >= 90:
        성적등급 = 'A'
        return 성적등급
    elif 점수 >= 80:
        return 'B'
    elif 점수 >= 70:
        return 'C'
    elif 점수 >= 60:
        return 'D'
    else:
        return 'F'

items = [1, 2, 3]
for i in items:
    print(f'변수i의 값은 {i}')

과일들 = ["사과", "배"]

for 과일 in 과일들:
    print(f'과일이름은 {item} 입니다.')
    # print(f'{}번째 과일은 {item} 입니다.')

for i in range(0, len(과일들)):
    print(f'과일이름은 {과일들[i]} 입니다.')
    print(f'{1}번째 과일은 {item} 입니다.')

for idx, 과일 in enumerate(과일들): #zip
    print(f'과일이름은 {과일} 입니다.')
    print(f'{idx}번째 과일은 {item} 입니다.')