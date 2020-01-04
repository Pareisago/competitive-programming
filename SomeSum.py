import fileinput

file = fileinput.input("test.txt")
line = int(file.readline())

if line == 1 or line == 3 or line == 5 or line == 7 or line == 9:
    print('Either')
elif line == 2 or line == 6 or line == 10:
    print('Odd')
elif line == 4 or line == 8:
    print('Even')

# if line == 1:
#     print('Either')
#     exit()
#
# if line == 2:
#     print('Odd')
#     exit()
#
# if line == 3:
#     print('Either')
#     exit()
#
# if line == 4:
#     print('Even')
#     exit()
#
# if line == 5:
#     print('Either')
#     exit()
#
# if line == 6:
#     print('Odd')
#     exit()
#
# if line == 7:
#     print('Either')
#     exit()
#
# if line == 8:
#     print('Even')
#     exit()
#
# if line == 9:
#     print('Either')
#     exit()
#
# if line == 10:
#     print('Odd')
#     exit()
