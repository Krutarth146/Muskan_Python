if "":
    print("False")
else:
    print("True")



# Truthy Values ---> True, 89, -90.89, [10,20], "Aman"
# Falsy Values ----> False, 0, [], ""


num = 0

if num > 0:
    print("Positive")
elif num < 0 :
    print("Negative")
else:
    print("Zero")


num1, num2 = 90,89

if num1 > num2:
    print("Num1 is Max")
else:
    print("Num2 is Max")



num3 = 77
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)


max1 = num1 if num1 > num2 else num2
max1 = (num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2 > num3 else num3)
print(max1)   # 90


choice = 90

match choice:
    case 1: print("Hello")

    case x: print("Invalid")




# While Loop

# start, End, Flow

_1 = 100

while _1 >= 25:
    print(_1,end=' ')
    _1 -= 2


# 66 * 81 = ?
# 66 * 82 = ?


# 28 ---> 1+2+4+7+14

# Twin Number ---> 2


num1 = 


i = 2

while i<num1:
    if num1 % i == 0:
        break
    i+=1

if i==num1:
    print("Prime")
