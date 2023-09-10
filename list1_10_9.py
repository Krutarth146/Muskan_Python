list1 = [10, 90, 56, 56, 89, 56, 67]
num = 56

# print(list(set(list1)))

new1 = []

for i in list1:
    if i not in new1:
        new1.append(i)

print(new1)   # [10, 90, 56, 89, 67]


for i in list1:
    if list1.count(i) == 1:
        print(i)


list1 = [(10,903), (34,), (3,78), (75,445), (20,1), (45,90)]
ans = [(34,), (45,90)]

for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j])