# Type - 2   with args and without Return Type


def muskan(n1, n2, n3 = 90):   # Defualt Function
    print(n1+n2 +n3)

muskan(10,20,30)   # 60


def Royal(ipl):
    # ipl()
    print('Royal FUnction')
    # return ipl()
    return ipl

def WorldCup():
    print('India Wins')
    return 90

ans = Royal(WorldCup)  
print(ans())   # 90


# ---------------------------------------------------
# public static void main(String args[])


# void main(String mus[])

# javac m.java Manoj 90


def Bank(doc, *args, rupees = 800):
    print(args)      # ('pan', 'aadhar', 900)
    print(type(args))  # <class 'tuple'>

    print(args[1])  # 900
    
Bank('pan','aadhar', 900) 


# **kwargs

dict1 = {'Name' : 'Muskan', 'roll' : 900, 'address' : {'City' : ['Ahm', 'Gnr']}}   # Ordered , No Index

print(dict1)   # {'Name': 'Muskan', 'roll': 900, 'address': {'City': ['Ahm', 'Gnr']}}


print(dict1.keys())   # dict_keys(['Name', 'roll', 'address'])

keys = [i for i in dict1.keys()]
print(keys)   # ['Name', 'roll', 'address']
print(len(dict1))   # 3

print(dict1.values())   # dict_values(['Muskan', 900, {'City': ['Ahm', 'Gnr']}])

print(dict1['address']['City'][0])   # Ahm
print(dict1['address']['City'])   # ['Ahm', 'Gnr']

for key,val in dict1.items():
    print(key, '----->', val)

# print(dict1[900])  # Error

mus = [key for key,val in dict1.items() if val == 900]
print(mus)   # ['roll']

dict1['Name'] = 'Arin'
print(dict1)   # {'Name': 'Arin', 'roll': 900, 'address': {'City': ['Ahm', 'Gnr']}}
   

def krutarth(n1,*kru, **kwargs):
    print(kwargs)   # {'name': 'Krutarth Patel', 'roll': 900, 'address': 'Ahm'}  Type - dict

    print(kwargs['address'])   # 900
    print(kru)

krutarth(10,20,30,name = 'Krutarth Patel', roll = 900, address = {'City' : 'Ahm', 'Roll' : 67}, name1 = 'Krutarth Patel')


# Type - 3,4

def Royal():
    return 90,80,20,89+23, 'Check'

Royal()
print(Royal())   # (90, 80, 20, 112, 'Check')
print(Royal()[-1][-3])   # e


# ------------------------------------------


def Factorial(num):
    mul = 1

    for i in range(1,num + 1):
        mul *= i

    return mul

Factorial(5)   # 120
print(Factorial(10))   # 3628800

# ------------------------------

def series(end):
    list1 = []
    for k in range(1,end+1):
        list1.append(k)
    return list1

print(series(10))   # 1



# ------------------------------

def series(end):
    for k in range(1,end+1,2):
        yield k

# Generator
# print(series(10))      # <generator object series at 0x0000021155BC5EE0>

# x = series(10)
# print(x.__next__())   # 1
# print(x.__next__())   # 2
# print(x.__next__())   # 3
# print(x.__next__())   # 4

# for i in (10,20,30,40):
for i in series(10):
    print(i)

for i in series(10):
    print(i)


# lambda, map, reduce, filter