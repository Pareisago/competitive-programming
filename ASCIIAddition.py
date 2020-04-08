import fileinput

num0 = "xxxxxx...xx...xx...xx...xx...xxxxxx"
num1 = "...x....x....x....x....x....x"
num2 = "xxxxx....x....xxxxxxx....x....xxxxx"
num3 = "xxxxx....x....xxxxxx....x....xxxxxx"
num4 = "x...xx...xx...xxxxxx....x....x....x"
num5 = "xxxxxx....x....xxxxx....x....xxxxxx"
num6 = "xxxxxx....x....xxxxxx...xx...xxxxxx"
num7 = "xxxxx....x....x....x....x....x....x"
num8 = "xxxxxx...xx...xxxxxxx...xx...xxxxxx"
num9 = "xxxxxx...xx...xxxxxx....x....xxxxxx"
numplus = ".......x....x..xxxxx..x....x......."

i = 0
b = 5

storednum1 = ""
storednum2 = ""
total = ""

while b < 500:
    file = fileinput.input("test.txt")
    number = ""
    for line in file:
        number += line[i:b]

    if number == num0:
        total = total + '0'
    if number == num1:
        total = total + '1'
    if number == num2:
        total = total + '2'
    if number == num3:
        total = total + '3'
    if number == num4:
        total = total + '4'
    if number == num5:
        total = total + '5'
    if number == num6:
        total = total + '6'
    if number == num7:
        total = total + '7'
    if number == num8:
        total = total + '8'
    if number == num9:
        total = total + '9'
    if number == numplus:
        storednum1 += total
        total = ""

    i += 6
    b += 6

finaltotal = int(storednum1) + int(total)

x = 0
z = 6
print(finaltotal)
for char in str(finaltotal):
    print('')
    for char in str(finaltotal):
        if char == "0":
            print(num0[x:z], end="")
        if char == "1":
            print(num1[x:z], end="")
        if char == "2":
            print(num2[x:z], end="")
        if char == "3":
            print(num3[x:z], end="")
        if char == "4":
            print(num4[x:z], end="")
        if char == "5":
            print(num5[x:z], end="")
        if char == "6":
            print(num6[x:z], end="")
        if char == "7":
            print(num7[x:z], end="")
        if char == "8":
            print(num8[x:z], end="")
        if char == "9":
            print(num9[x:z], end="")
    x += 6
    z += 6

print(' ')

a = """
xxxxx
x...x
x...x
x...x
x...x
x...x
xxxxx
"""
b = """
....x
....x
....x
....x
....x
....x
....x
"""

dice_art = [a, b]

for l in zip(*lines):
    print(*l, sep='')