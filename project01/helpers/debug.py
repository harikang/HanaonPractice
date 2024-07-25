def pp(*items):  # *a : 위치 인자
    for item in items:
        print("type is ", type(item))
        print()
        print("I can print ", item)


def pp_with_exit(*items):  # *a : 위치 인자
    for item in items:
        print("type is ", type(item))
        print()
        print("I can print ", item)

    import sys
    sys.exit()
