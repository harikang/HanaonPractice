nums = ["12", "12215", "123", "242", "12812", "123", "555", "34121"]
filtered = filter(lambda x: len(x) == 3, nums)
print(list(filtered))


def lenFilter(x):
    if len(x) == 3:
        return True

    return False


filtered = filter(lenFilter, nums)
print(list(filtered))


def two_x(num):
    return num * 2


숫자들 = [1, 2, 3, 4, 5]
mapped = map(two_x, 숫자들)
print(list(mapped))


def testFunc(a, b, c) -> str:
    """함수에 대한 설명

    Args:
        a (hkjhk): hkjhk
        b (hkjh): hkjh
        c (hkj): hkj

    Returns:
        str: 문자열 리턴
        """


print(testFunc.__doc__)
print(testFunc.__annotations__)
