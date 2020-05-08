import random
# ints = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

myset = set()
# for item in ints:
#     for item2 in ints:
#         for item3 in ints:
#             val = item + item2 + item3
#             if val == 10:
#                 sum += 1

while len(myset) < 10000:
    int1 = random.randint(-1, 50)
    int2 = random.randint(-1, 50)
    int3 = random.randint(-1, 50)
    finalint = int1 + int2 + int3
    if finalint == 10:
        tuple1 = (int1, int2, int3)
        myset.add(tuple1)
        print(len(myset))

import itertools
# letters = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']
#
# n = 0
# count = 0
# total = 0
# palinset = set()
# while n < 10000000:
#     word = ''
#     while len(word) < 6:
#         word += letters[random.randint(0,10)]
#     if word == word[::-1]:
#         print(len(palinset))
#         palinset.add(word)
#     n += 1
#
# print('TOTAL')
# print(len(palinset))