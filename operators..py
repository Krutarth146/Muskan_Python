# num1 = int(input())
# num2 = int(input())

# print(num1 + num2)


# Operators

# 1. Arithmetic O/p  + - * / // **

print(25 / 2)     # 12.5  (Float)
print(25 // 2)    # 12 (Floor)
print(-13 // 2)    # -7
print(25 * 2)
print(25 ** 2)  # 25 * 25  ---> 625

print(2**2**3)   # 2 ** 8 ---> 256  (Right to left)



# Assignment O/p  = += -= *= /= //= %= <<= >>= ^= |= &=  (Low Priority)

x = 10

x+=10   # x = x + 10
print(x)   # 20

x*=20   # x = x*20
print(x)   # 400


x/=10  # 40.0
x-=310 # -270.0
x+=23  # -247.0
print(x)
x%=3   # 2.0

print(x)

# -----------------

print(~90)    # -91
print(~-90)   # 89


# Bitwise O/p   & | ^ << >> ~
 
# & (Bitwise and)
# && --> and  (Logical)
# || --> or (Logical)

# & Table  (A*B)

# 0 0 -> 0
# 0 1 -> 0
# 1 0 -> 0
# 1 1 -> 1


# | Table (A+B)

# 0 0 -> 0
# 0 1 -> 1
# 1 0 -> 1
# 1 1 -> 1


# ^ Table (A^B)   ---> Same = 0

# 0 0 -> 0
# 0 1 -> 1
# 1 0 -> 1
# 1 1 -> 0

print(34 & 67)  # 2
print(45 | 211) # 255
print(12 ^ 562) # 574
print(12 << 5)  # 384
print(893 >> 2) # 223

print(0b101011)   # 43
print(0o101011)   # 33289
print(0xA)   # 10

print(bin(78))  # 0b1001110


# logical O/p   and or not

# Truthy Values --> 90, -10, 90.89, "Muskan", [10,20], True
# Falsy Values  --> False, '', [], 0


# Comparison O/p --->   <, >, <=, >= , ==, != 

if 10 % 2 == 0 or 25 % 5 == 0 and 66 % 4 == 0:
    print(True)


# Start, End, Flow

_a = 11

while _a <= 100:
    if _a % 5 == 0:
        print(_a,end=' ')
    _a +=1

# 1 0 1 1  --> 1

# 56 * 89 = ?
# 56 * 90 = ?
#      96

if not 5:
    print(True)
else:
    print(False)


# Membership O/p   ---> in , not in

list1 = [10, 90.89, "str1", 788, 56, [10,20,30,(10,20)], {10,20}, {"Name" : "Muskan"}]

# Linear Search

user_need = 7881

for royal in list1:
    if royal == user_need:
        print("Element is Found")
        break
else:
    print("Not Found")

# -------------------------------

if user_need in list1:
    print("ELment is Found")
else:
    print("Not FOund")


# Identity O/p  is , is not

x = 90
y = 90

if x == y:
    print("Same")

print(id(x), id(y))

if x is y:   # Reference Matching
    print("Same")


l1 = [10,20,30]
l2 = [10,20,30]

if l1 == l2:
    print("Same---------------")

print(id(l1), id(l2))

if l1 is l2:   # Reference Matching
    print("Same")