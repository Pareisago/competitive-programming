def mystery(a, b):
    if a == 1:
        return b
    else:
        return b+mystery(a-1, b)


print(mystery(5, 5))
