list1 = []
for i in range(0, 100):
    if i % 2 == 0:
        list1.append(i)

list2 = [x for x in range(0, 100) if x > 10]

print(list1)
print(list2)

list3 = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
print(list3)

guguList = [f"{i} * {j} = {i * j}" for i in range(2, 10, 2) for j in range(1, 10)]
for gugu in guguList:
    print(gugu)