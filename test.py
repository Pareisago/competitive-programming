def Max(L):
    if len(L) <= 1:
        return L[0]
    else:
        m = Max(L[1:])
        if m > L[0]:
            return m
        else:
            return L[0]


L = [1, 2, 3, 4, 5, 10, 7, 8, 9]

print(Max(L))