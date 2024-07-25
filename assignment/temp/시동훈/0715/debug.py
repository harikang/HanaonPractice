def pp(*items):
    for item in items:
        print(item)
        print("======>", type(item))
        import sys
        sys.exit()

