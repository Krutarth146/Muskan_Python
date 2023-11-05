# Recursion ---> When Func. Calls itself then it is Called as Recursion

def Series(num):
    if num == 1:   # Base Condition
        return 1
    print(num,end=' ')
    return Series(num - 1)  # Series(99)
    # return 1


print(Series(100))


# -------------------------------------

# Factorial 

def Factorial(num):
    # 5 * 4 * 3 * 2 * 1
    if num == 1:
        return 1
    return num * Factorial(num - 1)  # 5 * 4

import time
before_time = time.time()
print(Factorial(10))
print(time.time() - before_time)


def Fibonnacci_Iter(num):
    list1 = [1,1]

    for j in range(num-2):
        list1.append(list1[-1] + list1[-2])
    return list1[-1]

print(Fibonnacci_Iter(5))  # 5


# Binary Search

list1 = [120, 56, 89, 78, 42 , 56, 442]

# Binary Search 


# 1st Rule Sorting

list1.sort()
print(list1)  # [42, 56, 56, 78, 89, 120, 442]

need = 130

min = 0   # Ind
max = len(list1) - 1   # Index


while min <= max:
    mid = (min + max) // 2   # mid Index   5
    if need == list1[mid]:   # 120 == 78
        print(f"Element is Found at {mid} Index")
        break

    elif need < list1[mid]:  # 120 < 78 
        max = mid - 1

    elif need > list1[mid]:  # 120 > 78
        min = mid + 1           # min = 4

else:
    print("Not Found")



# -------------------------------------------------


def Muskan(Spiritual):
    def kru(Ashok):
        print("This is kru Function")
        Ashok()
    print("Muskan F")
    return kru(Spiritual)

@Muskan   # User Defined Decorator
def Geeta():
    print("Bhagwat Katha")

@Muskan
def Ramayan():
    print("Ramayan")


# @classmethod
# def manaoj(cls):
#     pass

# Muskan(Geeta)  # 100


# -------------------------

def Manoj():
    def kru():
        print("Kru Function")
        return [10,20,30]
    return kru

print(Manoj()()[2])  # 30

# x = Manoj()
# x()