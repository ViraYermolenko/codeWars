# def square_digits(num):
#     a = []
#     while num > 0:
#         a.append(num % 10)
#         num //= 10
#
#     a.reverse()
#
#     for x in range(len(a)):
#         a[x] = a[x]*a[x]
#
#
#     res = int(''.join(map(str, a)))
#     print(res)


def square_digits(num):
    return int(''.join([str(int(x) ** 2) for x in list(str(num))]))


print(square_digits(9119))


def square_digits2(num):
    squares = ''
    for x in str(num):
        squares += str(int(x) ** 2)
    return int(squares)


print(square_digits2(8117))