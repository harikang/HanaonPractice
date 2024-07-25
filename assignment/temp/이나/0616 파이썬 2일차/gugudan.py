for i in range(0, 101):
    print(i)

i = 0
while i <= 100:
    print(i)
    i += 1

for i in range(0, 101):
    if i % 2 == 0 and i != 0:
        print(i)

i = 0
while i <= 100:
    if i % 2 == 0 and i != 0:
        print(i)
    i += 1

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")

i = 2
j = 1
while i < 10:
    while j < 10:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1
    j = 1