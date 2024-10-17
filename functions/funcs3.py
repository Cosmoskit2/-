def multiple(*args):
    a = 1
    for i in args:
        a *= i
    print(args)
    return a


print(multiple(2, 3, 5))