import math

def hotpockets():
    #runtests()
    print("main")
    f=open("./10")
    runfile(f.read().splitlines())
    f.close()

def runtests():
    f=open("./10t")
    for i in f.read().split("pizza"):
        print("test")
        runfile(i.splitlines())
    f.close()

def runfile(file):
    if file[0] == '':
        file = file[1:]
    w = len(file)
    h = len(file[0])
    count = sum([1 for i in file for r in i if r == "#"])
    space = []
    for i in file:
        row = []
        for r in i:
            row.append(0 if r == "." else 1)
        space.append(row)
    high = 0
    for y in range(w):
        for x in range(h):
            if space[y][x] == 1:
                space[y][x] = count - subtract(x, y, space)
                if space[y][x] > high:
                    point = x,y
                    high = space[y][x]                  
    print(high)
    print(point)
    ang = {}
    for i in range(w):
        for j in range(h):
            if file[j][i] == "#":
                a = -angle(i, point[0], j, point[1])
                if a < -math.pi/2: #q2
                    a += math.pi * 2
                if a in ang:
                    ang[a].append((i,j))
                else:
                    ang[a] = []
                    ang[a].append((i,j))
    for a in ang:
        ang[a] = sorted(ang[a], key=lambda x: dist(point[0], x[0], point[1], x[1]))  
    print(ang.items())
    ang = sorted(ang.items(), key=lambda x: x[0])
    print(ang)
    count = 0
    while count < 200:
        for a in ang:
            if len(a[1]) > 0:
                val = a[1][0]
                a[1].remove(a[1][0])
                count += 1
                if count == 200:
                    print(val)


def angle(x1, x2, y1, y2): 
    #y is in the wrong direction
    return math.atan2(y2-y1, x1-x2)

def dist(x1, x2, y1, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
def subtract(x, y, space):
    ud = len(space)
    lr = len(space[0])
    marked = [[0 for i in range(len(space[0]))] for x in range(len(space))]
    marked[y][x] = 1
    for i in range(-ud, ud):
        for j in range(-lr, lr):
            if i != 0 or j != 0:
                startx = x
                starty = y
                seen = 0
                if startx + j >= 0 and startx + j < lr and starty + i >= 0 and starty + i < ud:
                    while startx + j >= 0 and startx + j < lr and starty + i >= 0 and starty + i < ud:
                        if space[starty+i][startx+j] > 0: 
                            seen = 1
                        startx += j
                        starty += i
                        if startx + j >= 0 and startx + j < lr and starty + i >= 0 and starty + i < ud and space[starty+i][startx+j] > 0 and seen == 1:
                            marked[starty+i][startx+j] = 1
    count = sum([1 for i in marked for r in i if r == 1])
    return count

hotpockets()

