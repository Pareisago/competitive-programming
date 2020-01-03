def AVLnodes(height):

    if (height == 0):
        return 1
    elif (height == 1):
        return 2

    return (1 + AVLnodes(height - 1) +
            AVLnodes(height - 2))


if __name__ == '__main__':
    H = 14
    print(AVLnodes(H))
