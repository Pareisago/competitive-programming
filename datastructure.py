import fileinput

file = fileinput.input()

mylist = []
slist = []


def check():
    # print(mylist)
    # print(slist)

    if len(slist) > len(mylist):
        print("impossible")
        mylist.clear()
        slist.clear()
        return


    s = 0
    q = 0
    p = 0
    z = 0
    
    #stack
    length = len(slist)
    revlist = mylist[::-1]
    # print(revlist[:length])
    if revlist[:length] == slist:
        s = 1
    
    #queue
    length = len(slist)
    # print(mylist[:length])
    if mylist[:length] == slist:
        q = 1
    
    #pq
    mylist.sort(reverse=True)
    length = len(slist)
    # print(mylist[:length])
    if mylist[:length] == slist:
        p = 1
    
    # print(s, q, p)
    z = s + q + p

    if s == 0 and q == 0 and p == 0:
        print("impossible")
    
    elif z > 1:
        print("not sure")
    
    elif p == 1:
        print("priority queue")
    
    elif s == 1:
        print("stack")
    
    elif q == 1:
        print("queue")
    
    mylist.clear()
    slist.clear()

i = 1
for line in file:
    line = line.strip().split()
    
    if len(line) == 1:
        count = int(line[0])
        continue

    if int(line[0]) == 1:
        mylist.append(int(line[1]))
    
    if int(line[0]) == 2:
        slist.append(int(line[1]))
    
    if i == count:
        check()
        i = 0
    i += 1