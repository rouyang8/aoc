import re

def chicken():
    f=open("./6t.txt")
    for (x,i) in enumerate(f.read().split("pizza")):
        print("test", x)
        run(i.strip().splitlines())
    f.close()
    print("main:")
    f=open("./6.txt")
    run(f.read().splitlines())
    f.close()

def run(file):
    lines = [re.match("([a-zA-Z0-9]+)\)([a-zA-Z0-9]+)", st).groups() for st in file]
    s = dict([(p1, p2) for (p2, p1) in lines])
    count = 0
    for inst in s:
        if inst != 'COM':
            temp = inst
            while temp != "COM":
                temp = s[temp]
                count += 1
    print(count)
    pyou = []
    psan = []
    for inst in s:
        if inst == 'YOU':
            while inst != "COM":
                inst = s[inst]
                pyou.append(inst)
        if inst == "SAN":
            while inst != "COM":
                inst = s[inst]
                psan.append(inst)
    print(len([i for i in pyou if i not in psan]) + len([i for i in psan if i not in pyou]))

chicken()
