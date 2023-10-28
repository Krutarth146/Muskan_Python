
# x = 10
# def muskan():
#     global x
#     b = x + 10
#     print(b)

#     c = 60
#     x = x + c
#     print(x, b)

# muskan()


# x = 'Muskan'

# assert x == 'muskan', "Did u mean Muskan"

# lambda -----> Anoumous function

def square(num):
    return num ** 2

print(square(3))   # 9

mus = lambda num : num ** 2
print(mus(4))   # 16

kru  = lambda x, y, z : (x if x > z else z) if x > y else (y if y > z else z)

print(kru(10,20,90))

# ---------------------------------------------

# Quadratic Function  (a * x ** 2)  + (b*x) + (c)


def quadratic_fun(a1,b1,c1):
    return lambda x : (a1 * x ** 2)  + (b1*x) + (c1)


royal = quadratic_fun(10,20,30)
print(royal(5))   # 380


# Nested lambda

g = lambda a1,b1,c1 = 30 : lambda x = 5 : (a1 * x ** 2)  + (b1*x) + (c1)

# m = g(10,20,30)

# print(m(5))

print(g(10,20,30)(5))
print(g(10,20)(5))
print(g(10,20)())  # 380


# ------------------------------------------------------------

# Map Function

list1 = [10,20,30,40,505,60]

square = lambda x : x**2

def sq(n):
    return n**2

for i in list1:
    print(square(i))

x = map(square, list1)
x = map(lambda x : x**2, list1)
x = list(map(sq, list1))
x = list(map(lambda x : (x**3) + 500, list1))

print(x)   # [100, 400, 900, 1600, 255025, 3600]

# n-zec Error

# x = int(input())
# y = int(input())

# print(x, y)

# f = input().strip().split()  # list
# b,n  = input().strip().split()  # 2 3
# print(f)
# print(b,n)


# m = list(map(ord, [x for h in input().split() for x in h]))

# print(m)


# filter

# even = list(filter(lambda x:x % 2 == 0 , [10,20,30,40,53,99]))
# odd = list(filter(lambda x : x % 2, [10,20,30,40,53,99]))
# odd = list(filter(lambda x : x & 1, [10,20,30,40,53,99]))
odd = list(filter(lambda x : x > 60, [10,20,30,40,53,99]))
# odd = list(map(lambda x : x % 2, [10,20,30,40,53,99]))   # [0, 0, 0, 0, 1, 1]

print(odd)   # [53, 99]


# reduce

from functools import reduce

sum = reduce(lambda x, y : x+y , list1)

print(sum)   # 665


from itertools import accumulate

x = list(accumulate(list1, lambda x, y : x+y))
print(x)  # [10, 30, 60, 100, 605, 665]

# recursion