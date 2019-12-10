import re
from itertools import permutations
from copy import deepcopy

def runfile(file):
    v = list(map(int, re.findall('([\-0-9]+)', file)))
    for i in range(2000):
        v.append(0)
    run(2, v)

def hotpockets():
    f=open("./9t.txt")
    for i in f.read().split("pizza"):
        print("test")
        runfile(i)
    f.close()
    print("main")
    f=open("./9.txt")
    runfile(f.read())
    f.close()

def args(val, i, ops, v):
    if ops[val-1] == 0:
        return v[v[i+val]]
    elif ops[val-1] == 1:
        return v[i+val]
    else:
        return v[v[-1] + v[i+val]]

def sto(val, i, ops, v):
    if ops[val-1] == 0:
        return v[i+val]
    else:
        return v[-1] + v[i+val]

def calc(ins, i, v, ops, inp): #calc
    steps = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    if ins == 1:
        v[sto(3, i, ops, v)] = args(1, i, ops, v) + args(2, i, ops, v)
    elif ins == 2:
        v[sto(3, i, ops, v)] = args(1, i, ops, v) * args(2, i, ops, v)
    elif ins == 3:
        v[sto(1, i, ops, v)] = inp
    elif ins == 4:
        print(args(1, i, ops, v))
    elif ins == 5:
        if args(1, i, ops, v) != 0:
            return args(2, i, ops, v)
    elif ins == 6:
        if args(1, i, ops, v) == 0:
            return args(2, i, ops, v)
    elif ins == 7:
        if args(1, i, ops, v) < args(2, i, ops, v):
            v[sto(3, i, ops, v)] = 1
        else:
            v[sto(3, i, ops, v)] = 0
    elif ins == 8:
        if args(1, i, ops, v) == args(2, i, ops, v):
            v[sto(3, i, ops, v)] = 1
        else:
            v[sto(3, i, ops, v)] = 0
    elif ins == 9:
        v[-1] += args(1, i, ops, v)
    return i + steps[ins]
    
def run(input_num, v):
    ind = 0
    while v[ind] != 99:
        one, two, three = (0, 0, 0)
        if v[ind] <= 9:
            if v[ind] == 3:
                ind = calc(3, ind, 0, (one, two, three), input_num)
            else:
                ind = calc(v[ind], ind, v, (one, two, three), input_num)
        elif v[ind] > 9:
            inst = v[ind] % 100
            one, two, three = v[ind] // 100 % 10, v[ind] // 1000 % 10, v[ind] // 10000 % 10
            ind = calc(inst, ind, v, (one, two, three), input_num)

hotpockets()