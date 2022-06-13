import sys

inp = sys.stdin.readlines()

d = [0 for x in range(int(inp.pop(0).strip('\n'))+1)]

g = int(inp.pop(0).strip('\n'))

clubs = []

for x in range(g):
    clubs.append(int(inp.pop(0).strip('\n')))

for x in range(1, len(d)):
    for y in range(len(clubs)):
        if x-clubs[y] >= 0 and d[x-clubs[y]] != -1:
            outcome = d[x-clubs[y]]+1
            if outcome < d[x] or d[x] == 0:
                d[x] = outcome
    if d[x] == 0:
        d[x] = -1
            
            
if d[-1] == -1:
    print('Roberta acknowledges defeat.')
else:
    print(f'Roberta wins in {d[-1]} strokes.')