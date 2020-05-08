import fileinput
import itertools

file = fileinput.input("test.txt")


def checkexact(S, L):
    extraset = set()
    exact = 0
    d = 0
    i = len(S)
    while i <= len(L):
        newl = L[d:i]
        if newl == S:
            exact += 1
            extraset.add(newl)
        d += 1
        i += 1
    ans = [exact, extraset]
    return ans


def checkdel1(S, L):
    ourset = set()
    set1 = checkexact(S.replace('A', ''), L)[1]
    set2 = checkexact(S.replace('T', ''), L)[1]
    set3 = checkexact(S.replace('C', ''), L)[1]
    set4 = checkexact(S.replace('G', ''), L)[1]
    for item in set1:
        ourset.add(item)
    for item in set2:
        ourset.add(item)
    for item in set3:
        ourset.add(item)
    for item in set4:
        ourset.add(item)
    print(ourset)
    return len(ourset)


def checkin1(S, L):
    return 0


for line in file:
    if line[0] == '0':
        exact = 0
        del1 = 0
        in1 = 0
        print("YEAH")
        continue

    line = line.strip().split()
    S = line[0]
    L = line[1]

    exact = checkexact(S, L)[0]
    del1 = checkdel1(S, L)
    in1 = checkin1(S, L)

    print(str(exact), str(del1), str(in1))

