import fileinput

file = fileinput.input("test.txt")
line = file.readline()

dict = {'test':'case'}


dict['key'] = 100
print(dict.get('get'))
for item in dict:
    print(item)

# print(len(line))
# print(line[9])

# for line in file:
#     print(line)

# for char in line:
#     if char == ' ':
#         print("YES")
#     else:
#         print(char)