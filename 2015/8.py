def main():
    print("test")
    run("./src/2015/t.txt")
    print("main")
    run("./src/2015/8.txt")
    

def run(file):
    f = open(file)
    lines = f.read().splitlines()
    escape = ["\\" + '\"', "\\" + "\\", "\\" + "x", "|"]
    full = 0
    morefull = 0
    for i, l in enumerate(lines):
        full += len(l)
        lines[i] = lines[i].replace(escape[1], "||||")
        lines[i] = lines[i].replace(escape[0], "||||")
    for l in lines:
        morefull += len(l) + l.count(escape[2]) + 4
        #print(morefull)
    print(full)
    print(morefull)
    print(morefull-full)

main()