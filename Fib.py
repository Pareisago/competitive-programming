from collections import Counter
c = Counter()


def fib(n):
    print(n)
    c[n] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x = fib(n-1)
        y = fib(n-2)
        return x + y


fib(8)
print(c)
