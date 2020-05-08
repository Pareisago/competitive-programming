
def math(integer):
    calc = (integer-1)*(integer)*(integer+2)
    if calc % 2 == 0:
        pass
    else:
        print('AHHH')


if __name__ == '__main__':
    z = 0
    while z < 100:
        math(z)
        z += 1
