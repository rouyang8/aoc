import re
from itertools import permutations
from copy import deepcopy

def runfile(file):
    v = list(map(int, re.findall('([\-0-9]+)', file)))
    letters = ['a','b','c','d','e']
    res = []
    for p in list(permutations(range(5,10))):
        amp = {a: deepcopy(v) for a in letters}
        r = {a: 0 for a in letters} #resume indexes
        o = {a: 0 for a in letters} #output
        first = True
        while o['e'] != -1:
            final = o['e']
            for i,l in enumerate(letters):
                if l == 'a':
                    o[l], r[l] = run(o['e'], amp[l], r[l], first, p[i])
                else:
                    o[l], r[l] = run(o[chr(ord(l)-1)], amp[l], r[l], first, p[i])
            first = False
        res.append(final)
    print(max(res))

def hotpockets():
    f=open("./7t.txt")
    for i in f.read().split("pizza"):
        print("test")
        runfile(i)
    f.close()
    print("main")
    f=open("./7.txt")
    runfile(f.read())
    f.close()

def donuts(ins, num1, num2, i, v):
    steps = [0, 4, 4, 2, 0, 3, 3, 4, 4]
    if ins == 1:
        v[v[i+3]] = num1 + num2
    elif ins == 2:
        v[v[i+3]] = num1 * num2
    elif ins == 3:
        v[v[i+1]] = num1
    elif ins == 4:
        return num1
    elif ins == 5:
        if num1 != 0:
            return num2
    elif ins == 6:
        if num1 == 0:
            return num2
    elif ins == 7:
        if num1 < num2:
            v[v[i+3]] = 1
        else:
            v[v[i+3]] = 0
    elif ins == 8:
        if num1 == num2:
            v[v[i+3]] = 1
        else:
            v[v[i+3]] = 0
    return i + steps[ins]
    
def run(input_num, v, resume, first, phase):
    ind = resume
    while v[ind] != 99:
        if v[ind] <= 8:
            if v[ind] == 3:
                if first == True:
                    ind = donuts(3, phase, 0, ind, v)
                    first = False
                else:
                    ind = donuts(3, input_num, 0, ind, v)
            elif v[ind] == 4:
                return v[v[ind+1]], ind+2
            else:
                ind = donuts(v[ind], v[v[ind+1]], v[v[ind+2]], ind, v)
        elif v[ind] > 8:
            inst = v[ind] % 100
            first = v[ind] // 100 % 10
            second = v[ind] // 1000 % 10
            num1 = v[v[ind+1]] if first == 0 else v[ind+1]
            num2 = v[v[ind+2]] if second == 0 else v[ind+2]
            if inst == "3":
                ind = donuts(int(inst), num1, num2, ind, v)
            elif inst == "4":
                return num1, ind+2, v
            else:
                ind = donuts(int(inst), num1, num2, ind, v)
    return -1, -1

hotpockets()