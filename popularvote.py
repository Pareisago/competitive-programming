import fileinput
file = fileinput.input('test.txt')
cases = int(file.readline())

i = 0
candidate = 1
summation = 0
maximum = 0
clearwinner = 1
mylist = []
sortlist = []

while i < cases:
    candidates = int(file.readline())
    for z in range(candidates):
        line = int(file.readline())
        mylist.append(line)
        if line > maximum:
            maximum = int(line)
    
    for item in mylist:
        summation += item

    newlist = mylist
    newlist.sort()
    
    for item in newlist:
        if item == maximum:
            clearwinner = 0
    if clearwinner == 0:
        print("no winner")
    elif (maximum / summation) >= 0.5:
        print("majority winner " + str(mylist.index(maximum) + 1))
    elif (maximum / summation) < 0.5:
        print("minority winner " + str(mylist.index(maximum) + 1))

    mylist = []
    sum = 0
    maximum = 0
    i += 1