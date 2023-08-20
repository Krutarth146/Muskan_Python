num = 2
step = 4

# 2 + 22 + 222 + 2222 === (?)


i=15
j=15
while i<=20:   # i = 16
    while j<=20:   # j = 16
        if i == j:  # 
            print(j,end=' ')   # 15
            j+=1
            break
        j+=1
    print(i,end=' ')   # 15
    i+=1



#  For Loop


# for(i=1 ; I,= 10 ; i++)

for i in range(10):
    print(i,end=' ')   # 0 1 2 3 4 5 6 7 8 9 

print()
for i in range(1,10):
    print(i,end=' ')   # 1 2 3 4 5 6 7 8 9 

    
print()
for i in range(10,1,1):
    print(i,end=' ')   # 1 2 3 4 5 6 7 8 9 

    
print()
for i in range(10,1,-1):
    print(i,end=' ')   # 10 9 8 7 6 5 4 3 2

print()
for i in range(-3,-9,-1):
    print(i,end=' ')   # -3 -4 -5 -6 -7 -8

print()
for i in range(-3,-9,1):
    print(i,end=' ')   # blank

    
print()
for i in range(-3,-9,-3):
    print(i,end=' ')   # -3 -6


print()

for i in range(78,83):
    for j in range(78,83):
        if i<j:
            print(j,end=' ')
            continue
    print(i,end=' ')


# while (num > 0)

# for( ; num > 0 ; )

for i in range(90):
    pass

while 90:
    pass
