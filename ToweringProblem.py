import fileinput
import itertools
from random import shuffle

file = fileinput.input()
line = file.readline()


def check(numbers, k):
    if numbers[0] > numbers[1] > numbers[2] and sum(numbers) == k:
        return True
    else:
        return False


line = [int(x) for x in line.split()]
numbers = line[0:6]

height1 = line[6]
height2 = line[7]

while True:
    shuffle(numbers)
    if check(numbers[0:3], height1) and check(numbers[3:6], height2):
        break

print(" ".join([str(x) for x in numbers]))

# perms = list(itertools.permutations(line))
# store = ''

# for item in perms:
#     if int(item[0]) > int(item[1]) and int(item[1]) > int(item[2]) and int(item[3]) > int(item[4]) and int(item[4]) > int(item[5]):
#         sum1 = int(item[0]) + int(item[1]) + int(item[2])
#         sum2 = int(item[3]) + int(item[4]) + int(item[5])
#         if sum1 == int(height1) or sum1 == int(height2):
#             if sum2 == int(height1) or sum2 == int(height2):
#                 if int(item[0]) > int(item[3]):
#                     for item in item:
#                         store += item + ' '
#
# print(store[:-1])
# exit()
