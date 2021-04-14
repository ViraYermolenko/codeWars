def stringy(size):
    res = []
    a = size
    for x, y in zip(range(0, a, 2), range(1, a, 2)):
        res = ([1] * x + [0] * y)
    return res


print(stringy(5))