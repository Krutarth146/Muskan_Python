# Python ---> Interpreted Lang., Dynamic (Run time)

print('Hello')
print("Muskan")
print('''
    Hello 
    Muskan
''')
print("Royal")

# int x;
# float y;  # Compile Time 

x = 90.90   # Runtime Compilation

x = "Str1"

print(x)  # str1
print(type(x))   # <class 'str'>

# Single Line Comment

'''
Multi
Line
Comment
'''

# print Statement -----------------

print('Muskan',end=' ROyal ')   # '\n'  default
print('Shekh')  # Muskan ROyal Shekh
# Hoisting

x = 10
y = 'str1'
z = True

print(x,y,z,sep='\t',end=' ')  # 10      str1    True

print(
    '''
    Royal Technosoft
    Sargasan
'''
)


name = 'Manoj'
rupees = 900

print(type(rupees))  # <class 'int'>

print('Manoj has 900 rupees only.')
print(name,'has',rupees,'rupees only.')

print("{} has {} rupees only.".format("Manoj", 800))
print("{1} has {0} rupees only.".format("Manoj", 800))  # 800 has Manoj rupees only.
print("{name} has {money} rupees only.".format(name = "Manoj", money = 800))  # 800 has Manoj rupees only.
print()

print(f"{name} has {rupees + 8500} rupees only.")   # fstring (Adv. Formatted String)  Manoj has 9400 rupees only.


# Datatypes and Typecasting

# Datatypes => int, float, string, bool, complex, Nonetype, List, Tuple, Set, Dict

x = 90000000000000000000000000000000000

print(x)
print(x.__sizeof__())  # 40

print(len(str(x)))   # 35   (starts from 1), Index starts from 0


print(type(x))   # <class 'int'>


x = 89

y = 89.32

print(x+y)   # int + float   # 178.32  # Implicit T.c

# Typecasting ---> 1. Implicit T.c  2. Explicit T.c


x = '32'
y = '32'

print(x+y)   # 3232

v = 32

print(x + str(v))  # 3232  # Explicit T.c



jk = True   # bool
ww = 90    # int

print(jk + ww)  # bool + int   91  # Implicit


z = '301.98'
print(int(float(z)))  #  301   # Explicit


print(round(301.98))   # 302
print(round(561.98,-3))   # 1000.0

import math
print(math.floor(301.98))   # 301
print(math.ceil(301.0001))   # 302
print(math.ceil(301.0000))   # 301

v = 89 + 6j   # 89 is real part and 6j is Imaginary Part
print(type(v))   # <class 'complex'>

k = 90
print(v+k)   # (179+6j)

# Input()

# scanf("%d",&num1);

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))

print(f"{num1} + {num2} = {num1 + num2}")   # 100 + 203 = 303


# Calc, 5 Area, Years, Seconds