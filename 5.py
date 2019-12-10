import re

def hotpockets():
    f=open("./5t.txt")
    for i in f.read().split("pizza"):
        print("test")
        run(i, 7)
    f.close()
    print("main")
    f=open("./5.txt")
    run(f.read(), 5)
    f.close()

def donuts(ins, num1, num2, i, v):
    if ins == 1:
        v[v[i+3]] = num1 + num2
        i += 4
    elif ins == 2:
        v[v[i+3]] = num1 * num2
        i += 4
    elif ins == 3:
        v[v[i+1]] = num1
        i += 2
    elif ins == 4:
        print(num1)
        i += 2
    elif ins == 5:
        if num1 != 0:
            i = num2
        else:
            i+=3
    elif ins == 6:
        if num1 == 0:
            i = num2
        else:
            i +=3
    elif ins == 7:
        if num1 < num2:
            v[v[i+3]] = 1
        else:
            v[v[i+3]] = 0
        i+=4
    elif ins == 8:
        if num1 == num2:
            v[v[i+3]] = 1
        else:
            v[v[i+3]] = 0
        i+=4
    return i
    
def run(file, input_num):
    v = list(map(int, re.findall('([\-0-9]+)', file)))
    ind = 0
    while v[ind] != 99:
        if v[ind] <= 8:
            if v[ind] == 3:
                ind = donuts(3, input_num, 0, ind, v)
            if v[ind] == 4:
                ind = donuts(4, v[v[ind+1]], 0, ind, v)
            else:
                ind = donuts(v[ind], v[v[ind+1]], v[v[ind+2]], ind, v)
        elif v[ind] > 8:
            st = str(v[ind])
            first = 0
            second = 0
            #third = 0
            if len(st) == 3:
                first = st[0]
            elif len(st) == 4:
                second = st[0]
                first = st[1]
            elif len(st) == 5:
                #third = st[0]
                second = st[1]
                first = st[2]
            inst = st[-1]
            num1 = v[ind+1]
            num2 = v[ind+2]
            if inst == "3" or inst == "4":
                ind = donuts(int(inst), num1, num2, ind, v)
            else:
                if int(first) == 0:
                    num1 = v[v[ind+1]]
                if int(second) == 0:
                    num2 = v[v[ind+2]]
                ind = donuts(int(inst), num1, num2, ind, v)

hotpockets()