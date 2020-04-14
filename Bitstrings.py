# def printTheArray(arr, n):
#     for i in range(0, n):
#         print(arr[i], end=" ")
#
#     print()
#
#
# def generateAllBinaryStrings(n, arr, i):
#     if i == n:
#         printTheArray(arr, n)
#         return
#
#     arr[i] = 0
#     generateAllBinaryStrings(n, arr, i + 1)
#
#     arr[i] = 1
#     generateAllBinaryStrings(n, arr, i + 1)
#
#
# if __name__ == "__main__":
#     n = 12
#     arr = [None] * n
#     generateAllBinaryStrings(n, arr, 0)

import fileinput
file = fileinput.input("output.txt")

q = 0
for line in file:
    line = line.strip().split()
    k = 0
    m = 0
    for item in line:
        if item == '1':
            k += 1
        if item == '0':
            m += 1
    if k == m:
        q += 1

print(q)
