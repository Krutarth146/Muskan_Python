# list1 = [[10,20,30], 
#          [40,80,90], 
#          [56,78,12]]


# print(list1[2][1])   # 78
# print(list1[2][-2])   # 78

# print(list1[2])
# print(list1[2][-1])  # 12
# print(list1[2][-3::1])  # [56, 78, 12]
# print(list1[2][-3:-1:1])  # [56, 78]

# list1 = [[10,20,30], 
#          [40,80,90], 
#          [56,78,12]]

# for sublist in list1:   # [10, 20, 30]
#     for ele in sublist:
#         print(ele,end=' ')
#     print()

# # --------------------------

# for row in range(len(list1)):  # 3
#     if row % 2 != 0:
#         # for ele in reversed(list1[row]):
#         #     print(ele,end=' ')
#         # for ele in list1[row][::-1]:
#         #     print(ele,end=' ')
#         for col in range(len(list1[row]) - 1, -1, -1):
#             print(list1[row][col],end=' ')
#     else:
#         for col in range(len(list1[row])):
#             print(list1[row][col],end=' ')
#     print()



# # 

# list1 = [10,20,30,40,50,30]
# list2 = [90,45,67,8,923,11]

# # j = 0
# # for i in range(len(list1)):
# #     while j<len(list2):
# #         print(list1[i],list2[j])
# #         j+=1
# #         break


# for k in zip(list1,list2):
#     print(k)

# # for val1,val2 in zip(list1,list1):
# #     print(val1,val2)
# #     if val2 == 30:
# #         print(val1)
    


# # list1 = [10,90,33,21,89,67,55,44]

# # # for j in range(len(list1)):
# # #     if list1[j] % 2 != 0:
# # #         print(j)


# # for ind,val in enumerate(list1,100):
# #     print(ind)

# # print(eval('3+2'))

# # 1.
# # a=[1,2,3,4,5,(4,5),"u",{"w":45,"r":21},5] 

# # output
# # 1
# # 2
# # 3
# # 4
# # 5
# # str u
# # tuple is: (4,5)
# # dictonary keys:w
# # dictonary values:45
# # dictonary keys:r
# # dictonary values:21
# # 5


# # 2. Div
# # 3. Spiral

# # List Comprehension

# list1 = [10,90,89,77]

# for i in list1:
#     if i % 2 != 0:
#         print(i)

# new = [i for i in list1 if i % 2 != 0]
# print(new)   # [89, 77]


# # [(10,1000), (20,8000), (5,125)]

# list7 = [(j,j**3) for j in list1]

# print(list7)   # [(10, 1000), (90, 729000), (89, 704969), (77, 456533)]

# list1 = [10,90,89,77]

# print([(i,j) for i in list1 for j in list1])


# # Aman
# # [['A','aaa'], ['M','mmm'] ....]
# # NayaN
# new1 = {x.upper() : (x.lower() * 3, chr(ord(x.lower())) * 3) for x in input()}
# print(new1)

inp = [i for i in input().strip().split(' ')]   # 10 20 30 40 50 60 70 80 90
print(inp)

str2 = 'Aman'

# [['A', 'AA'], ['M' , "MM"] ....]

list1 = [[10,90,343,89], [20,944,11,6], [33,9,3,1]]

ans = [[1,3,6,9], [10,11,20,33], []]