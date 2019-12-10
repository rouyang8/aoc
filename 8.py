from copy import deepcopy

def hotpockets():
    f=open("./8t.txt")
    for i in f.read().split("pizza"):
        print("test")
        runfile(i, 2, 2)
    f.close()
    print("main")
    f=open("./8.txt")
    runfile(f.read(), 25, 6)
    f.close()

def runfile(file, leng, height):
    a = [[0 for i in range(leng)] for i in range(height)]
    b = []
    ind = 0
    while ind < len(file):
        for i in range(height):
            for j in range(leng):
                a[i][j] = file[ind]
                ind += 1
        b.append(deepcopy(a))
    sums = []
    for i in b:
        d = 0
        for ix in i:
            d += ix.count('0')
        sums.append(d)
    layer = sums.index(min(sums))
    one = 0
    two = 0
    for i in b[layer]:
        one += i.count('1')
        two += i.count('2')
    print(one*two)
    final = []
    for i in range(height):
        line = []
        for j in range(leng):
            ind = 0
            while b[ind][i][j] == '2':
                ind += 1
            line.append(b[ind][i][j])
        final.append(line)
    for l in range(len(final)):
        for x in range(len(final[l])):
            if final[l][x] == '1':
                final[l][x] == ' '
    for l in final:
        print("".join(l))

        
    
    



hotpockets()

