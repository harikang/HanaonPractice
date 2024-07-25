for x in range(2,10):
    for y in range(1,10):
        print(x, '*', y, '=', x * y)
        if(y == 9):
            print('----------')


print("구구단 출력.\n")
for x in range(2, 10):
    print("------- [" + str(x) + "단] -------")
    for y in range(1, 10):
        print(x, "x", y, "=", x*y)
