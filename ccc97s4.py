import sys

def convert(x):
    x = x.strip('\n')
    a = ''
    for i in range(len(x)):
        if x[i] != '-':
            a += x[i]
    return a

def spl(x):
    return x.split(' ')

inp = list(map(convert,sys.stdin.readlines()))

n = int(inp.pop(0)[0])

inp = list(map(spl, inp))

d = []
#print(inp)
for x in range(len(inp)):
    if inp[x] == ['']:
        d = []
    else:
        for i in range(len(inp[x])):
            if inp[x][i] in d:
                inp[x][i] = str(d.index(inp[x][i])+1)
            else:
                d.append(inp[x][i])
for x in range(len(inp)):
    if inp[x] != ['']:
        print(' '.join(inp[x]))
    else:
        print('')