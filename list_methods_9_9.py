list1 = [10,20,90,78,46,23,12]

# List characteristics: Ordered (Indexed), Allow's Duplicates, Mutable (Changeble)


print(list1[-2]) # 23   # Indexing

# Slicing
print(list1[-2:5:1]) # []
print(list1[3:-2:1]) # [78, 46]
print(list1[-6:-1:]) # [20, 90, 78, 46, 23]
print(list1[::-1]) # [12, 23, 46, 78, 90, 20, 10]


# List Methods

list1 = [10,20,90,78,46,23,12]

list1.append('900')
list1.append([10,20])
print(list1)    # [10, 20, 90, 78, 46, 23, 12, '900', [10, 20]]

try: 
    list1.extend(100)   # TypeError: 'int' object is not iterable
except NameError:
    print("NameError")
except Exception as e:
    print("Int object is not allowed",e)   # Int object is not allowed 'int' object is not iterable


list1.extend('1000')
print(list1)   # [10, 20, 90, 78, 46, 23, 12, '900', [10, 20], '1', '0', '0', '0']


list2 = [10,90,89,78]

# list1.append(list2)
# print(list1)    # [10, 20, 90, 78, 46, 23, 12, '900', [10, 20], '1', '0', '0', '0', [10, 90, 89, 78]]

# list1.extend(list2)
# print(list1)   # [10, 20, 90, 78, 46, 23, 12, '900', [10, 20], '1', '0', '0', '0', 10, 90, 89, 78]


list1.extend([[10,20], [30,40]])
print(list1)  # [10, 20, 90, 78, 46, 23, 12, '900', [10, 20], '1', '0', '0', '0', [10, 20], [30, 40]]


list1.insert(2,900)
print(list1)

list1.insert(-1,900)
print(list1)   # [10, 20, 900, 90, 78, 46, 23, 12, '900', [10, 20], '1', '0', '0', '0', [10, 20], 900, [30, 40]]

print(len(list1))   # 17


list1[2] = "Manoj"
print(list1)


# list1[17] = 'Muskan'   # Error

list1.insert(17,9001)
print(list1)   # [10, 20, 'Manoj', 90, 78, 46, 23, 12, '900', [10, 20], '1', '0', '0', '0', [10, 20], 900, [30, 40], 9001]


# del list1
del list1[5:]

print(list1)   # [10, 20, 'Manoj', 90, 78]


print(list1.pop())
print(list1)  # [10, 20, 'Manoj', 90]


list1.pop(2)
print(list1)  # [10, 20, 90]


list1.remove(20)
print(list1)   # [10, 90]



list1.sort(reverse=True)
print(list1)


# list1.reverse()
# print(list1)   # [90, 10]

print(list1.count(10))   # 1
print(list1.index(10))   # 1


list2 = list1.copy()   # Xerox
list3 = list(list1)   # Xerox

list1.append("kk")
print(list2,list3)


list6 = list1


list6.append(902)
print(list1)   # [90, 10, 'kk', 902]


for x in list1:
    print(x)

for k in range(len(list1)):
    print(k, list1[k])


list1 = [10,20,30,40,50,60,70,80,90]

# Ans.1  [(10,10), (10,20) ,[10,30], [10,40], (10,50)....]
# Ans. 2 [[10],[10,20], [10,20,30], [10,20,30,40]]

# Ans.1  [(10,10), (10,20) ,[10,30], [10,40], (10,50)....]

ans = []

for i in range(len(list1)):  # 10
    for j in range(len(list1)):
        ans.append((list1[i], list1[j]))

print(ans)