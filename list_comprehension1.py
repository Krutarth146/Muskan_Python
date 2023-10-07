list1 = [10,20,30,40,51]

for j in list1:
    if j % 2 == 0:
        print(j)

list1 = [j for j in list1 if j % 2 == 0]
print(list1)  # [10, 20, 30, 40]



l1 = [10,90,20,30,40]
# ans = [(10,10), (10,90)....]

res = [(i,j) for i in l1 for j in l1]
print(res)


l2 = [10,90,23,45,67]
l3 = [10,92,21,334,67]

# for k in range(len(l2)):
#     for h in range(len(l3)):
#         if k == h:
#             print(l2[k], l3[h])


aman = [(k,h) for k,h in zip(l2,l3)]
print(aman)   # [(10, 10), (90, 92), (23, 21), (45, 334), (67, 67)]


rishita = [ele for ind, ele in enumerate(l2,100) if ind % 2 == 0]

print(rishita)   # [(0, 10), (1, 90), (2, 23), (3, 45), (4, 67)]


list1 = [10,90,45,67,23]

# ans = [(1,2,5,10), (1,2,3,5,6,9,10,15,45,90)....]
  

main = []
for ele in list1:
    temp = []
    for j in range(1,ele+1):
        if ele % j == 0:
            temp.append(j)
    main.append(tuple(temp))

print(main)   # [(1, 2, 5, 10), (1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90), (1, 3, 5, 9, 15, 45), (1, 67), (1, 23)]


r1 = (tuple(j for j in range(1,ele+1) if ele % j == 0) for ele in list1)
print(r1)  # [(1, 2, 5, 10), (1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90), (1, 3, 5, 9, 15, 45), (1, 67), (1, 23)]

print(r1.__next__())
print(r1.__next__())
print(r1.__next__())
    # print(tuple(i))

list1 = [(10,902), (23,78,99), (45,8), (34,), (12,90)]

k = 2

# ans = [(23,78), (34,), (12,90)]

main1 = []
for subtup in list1:
    x = [i for i in subtup if len(str(i)) == k]
    if len(x) == len(subtup):
        main1.append(subtup)

print(main1)   # [(23, 78), (34,), (12, 90)]


r3 = [subtup for subtup in list1 if len([i for i in subtup if len(str(i)) == k]) == len(subtup)]
print(r3)

res1 = [(10,90), (34,67), (55,667), (12,23)]

ans3 = [(12,23), (34,67), (10,90), (55,667)]