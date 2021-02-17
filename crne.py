import fileinput
file = fileinput.input("test.txt")
num = int(file.readline())

# val1 = num // 2 + 1
# val2 = num - (num//2) + 1
# result = val1 * val2
# cuts = lambda n: ((n//2)+1) * ((n-(n//2))+1)

if num % 2 == 0:
    cuts = (num // 2 + 1) ^ 2
else:
    cuts = (num - (num//2) + 1)

print(cuts)
# print(cuts(num))