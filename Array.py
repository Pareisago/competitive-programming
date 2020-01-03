
array = [1, 1, 1, 1, 1, 1]


def odd_zeroes(arr):
    pos = len(arr) - 1
    while pos > 0:
        arr[pos] = 0
        pos = pos - 2


odd_zeroes(array)
print(array)
