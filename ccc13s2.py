import sys

def test(i):
    return int(i.strip('\n'))

inp = sys.stdin.readlines()

maxw = int(inp.pop(0).strip('\n'))
trains = int(inp.pop(0).strip('\n'))

inp = list(map(test, inp))

if sum(inp[0:4])-inp[0:4].count(1) > maxw:
    print(0)
else:
    for x in range(trains):
        if len(inp[x:x+4]) < 4 or sum(inp[x:x+4]) > maxw:
            n = 3
            while sum(inp[x:x+n]) > maxw:
                n -= 1
            print(n+x)
            break