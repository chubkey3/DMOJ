import sys

def convert(x):
    x = x.strip('\n')
    a = ''
    for i in range(len(x)):
        if x[i] != '-':
            a += x[i]
    return list(a)

inp = sys.stdin.readlines()

k = [chr(x) for x in range(65, 91)]

a = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

n = int(inp.pop(0))

inp = list(map(convert, inp))

for x in range(n):
    for y in range(10):
        try:
            int(inp[x][y])
        except:
            inp[x][y] = a[k.index(inp[x][y])]
    inp[x].insert(3, '-')
    inp[x].insert(7, '-')
    print(''.join(list(map(str,inp[x][:12]))))