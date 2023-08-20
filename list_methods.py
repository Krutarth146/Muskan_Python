list1 = []

print(list1)
print(type(list1))   # <class 'list'>

lst = [10,20]
  
list1 = [10,10,20.90, 'D',"Dalpat",[(10,20), {10,20}], {'Name' : "Muskan"}]

print(list1)   # <class 'list'>
# [10, 10, 20.9, 'D', 'Dalpat', [(10, 20), {10, 20}], {'Name': 'Muskan'}]

print(len(list1))   # 7 ---> starts from 1, Index starts from 0
print(id(list1))   # 1562038714240

lst1 = [10,90,88,34.90]

print(max(lst1))   # 90
print(min(lst1))   # 90
print(sum(lst1))   # 222.9

print(sum(lst1) / len(lst1))   # 55.725


# List Characteristics: ---> Ordered (Indexed)


list1 = [10,20,30,40,50,60,70,80,890,[10,20,[203,90]]]

# (Indexing)

print(list1[4])   # 50
print(list1[-1])   # [10,20,[203,90]]
print(list1[-1][-1][1])   # 90

print(type(list1[-2]))   # <class 'int'>

list1 = [10,20,890,[10,20,[203,90]]]

# Slicing

# print(list1[start : end (n-1) : step(n-1)])

print(list1[2:-1:-1])   # []
print(list1[2:-1:1])   #  [890]
print(type(list1[2:-1:1]))   # <class 'list'>