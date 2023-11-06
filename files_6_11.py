# Modes :
# 'w' - write Mode (Overwrite)
# 'a' - Append Mode (Append)
# 'r' - Read Mode 
# 'x'
# 't' - Text File (\n \b \t)
# 'b' - Binary File

# f1 = open('muskan.txt', 'wt')

# f1.write("Hello My Name is Muskan Padhiyar")

# list1 = ['\nAman is Good Boy', '\nAhm is Best city Ever', '\nRoyal is Best Institute.']

# f1.writelines(list1)

# f1.close()

f1 = open('muskan.txt', 'w+')

# exit()
list1 = ['\nAman is Good Boy', '\nAhm is Best city Ever', '\nRoyal is Best Institute.']

f1.writelines(list1)

print(f1.tell())  # 67


f1.seek(0)
# x = f1.read()

# print(x)

# print(f1.readline(3))
# print(f1.tell())  # 0
# print(f1.readline())  # lo My Name is Muskan Padhiyar
# print(f1.tell())  # 34


# f1.seek(24)

# print(f1.readlines())

k = f1.read()
# print(k)

# list1 = k.split('\n')

# print(list1)

# c = 0
# for sen in list1:
#     x = sen.split(' ')
#     print(len(x))

#     for f in sen:
#         c+=1

# print(c)
# f1.close()




df = open("enquiry_Register.png", 'rb')

cb = df.read()

# print(cb)

df.close()

gw = open("other_copy.jpg","wb")

gw.write(cb)

gw.close()

# Pickle Module  (dumps, loads)