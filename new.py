import fileinput

file = fileinput.input()

dict = {}

for line in file:
    line = line.strip().split()
    if line[0] == "define":
        dict[line[2]] = int(line[1])
    elif line[0] == "eval":
        operator = line[2]
        if line[1] in dict:
            if line[3] in dict:
                left = dict.get(line[1])
                right = dict.get(line[3])

                if operator == "<":
                    if left < right:
                        print("true")
                    else:
                        print("false")
                
                if operator == ">":
                    if left > right:
                        print("true")
                    else:
                        print("false")
                    
                if operator == "=":
                    if left == right:
                        print("true")
                    else:
                        print("false")
            else:
                print("undefined")
                continue
        else:
            print("undefined")
            continue
        

