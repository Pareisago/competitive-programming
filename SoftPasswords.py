import fileinput


def identical(s, p):
    if s == p:
        return True


def prepend(s, p):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for item in numbers:
        new = ''.join((item, p))
        if new == s:
            return True


def append(s, p):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for item in numbers:
        new = ''.join((p, item))
        if new == s:
            return True


def reverse(s, p):
    new = ''
    for char in p:
        if char.isupper():
            new += char.lower()
        else:
            new += char.upper()
    if new == s:
        return True



if __name__ == "__main__":
    file = fileinput.input()
    s = file.readline()
    s = s.strip()
    p = file.readline()
    p = p.strip()

    if reverse(s, p) or prepend(s, p) or append(s, p) or reverse(s, p):
        print("True")
    else:
        print("False")