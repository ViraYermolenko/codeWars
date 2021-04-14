def pipe_fix(nums):
    nums.sort()
    print(nums)
    res = list(range(nums[0], nums[-1] + 1))
    return res


def is_odd(x):
    r = x / 2.0
    return True if r == int(r) and int(r) != 1 else False


def divisors(integer):
    div = [x for x in range(2, integer) if integer % x == 0]
    if len(div) == 0:
        return str(integer) + ' is prime'
    return [x for x in range(2, integer) if integer % x == 0]


def find_next_square(sq):
    if sq ** 0.5 == int(sq ** 0.5):
        return int(((sq ** 0.5) + 1) * ((sq ** 0.5) + 1))
    else:
        return -1


def divisors2(number):
    divider_list = []
    for divider in range(2, number):
        if number % divider == 0:
            divider_list.append(divider)
    if len(divider_list) == 0:
        return f"{number} is prime"
    return divider_list


def paperwork(n, m):
    return max(n, 0) * max(m, 0)


print(is_odd(2))
print(divisors(13))
print(find_next_square(121))
print(divisors(12))
print(divisors(25))
print(divisors2(13))
print(pipe_fix([1, 2, 3, 5, 6, 8, 9]))
#
# def pipe_fix(l):
#     return [x for x in range(min(l), max(l)+1)]
# def pipe_fix(nums):
#     return list(range(nums[0], nums[-1] + 1))

# def find_next_square(sq):
#     # Return the next square if sq is a square, -1 otherwise
#     if sq<1:
#         return -1
#     else:
#         for i in range(int(sq/2)+1):
#             if (i*i) == sq:
#                 return (i+1)*(i+1)
#             else:
#                 return -1
#
# print(find_next_square(121))

# def find_next_square(sq):
#     root = sq ** 0.5
#     if root.is_integer():
#         return (root + 1)**2
#     return -1


# def find_next_square(sq):
#     x = sq**0.5
#     return -1 if x % 1 else (x+1)**2


# import math
#
#
# def find_next_square(sq):
#     return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1


#
# def is_odd(a):
#     return bool(a & 1)


#
# def divisors(num):
#     l = [a for a in range(2,num) if num%a == 0]
#     if len(l) == 0:
#         return str(num) + " is prime"
#     return l
#
# def divisors(n):
#     return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n
