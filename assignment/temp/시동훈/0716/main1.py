from exam.exam import 성적처리

if __name == "__main__":
    print("성적을 입력하세요")
    사용자가 입력한성적 = input("성적입력: ")
    결과 = 성적처리(int(사용자입력성적))
    print(f("당신의성적등급은 {결과}입니다")


print(m)

for m in range(3):
    pass

n = 0
while True:
    print(f'변수 n의 값은 {n}')
    n += 1

0 100 출력 for while
짝수만 출력 for while

for i in range(0, 100):  # 0부터 100까지의 숫자 반복
    if i % 2 == 0:  # 짝수인지 확인
        print(i)  # 짝수인 경우 출력

for i in range(0, 100):
    print(i + 1)
포문 하고 와일문으로 출력

구구단 for while
for x in range(2, 10):
    for y in range(1, 10):
        print(x, '*', y, '=', x * y)
        if (y == 9):
            print('----------')