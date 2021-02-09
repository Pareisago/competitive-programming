import fileinput

file = fileinput.input()
for line in file:
    num = int(line)
    if num == 0:
        exit()
    dnum = 2*num
    
    bigdubprime = 0
    islittlenotprime = False
    
    p = 0
    while p == 0:
        for q in range(2, dnum):
            if (dnum % q) == 0:
                bigdubprime = dnum
                p = 1
                for z in range(2, num):
                    if (num%z) == 0:
                        islittlenotprime = True
                if islittlenotprime:
                    print(str(bigdubprime) + ' ('+ str(num)+ ' is not prime)')
                else:
                    print(bigdubprime)
                break
        dnum += 1