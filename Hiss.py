import fileinput


def main():
    file = fileinput.input("text.txt")
    for char in file:
        if char == 's':
            if char[char+1] == 's':
                print('hiss')


if __name__ == "__main__":
    main()
