import sys
from collections import deque

inp = sys.stdin.readlines()

n, m = list(map(int, inp.pop(0).strip('\n').split(' ')))

rates = deque([])
cars = deque([])
i = deque([])
spots = deque([])
queue = deque([])
money = 0

for x in range(n):
    rates.append(eval(inp.pop(0)))
    spots.append(None)
for x in range(m):
    cars.append(eval(inp.pop(0)))
for x in range(m*2):
    i.append(eval(inp.pop(0)))
    
for x in range(len(i)):
    if i[x] > 0:
        if None not in spots:
            queue.append(i[x])
        else:
            k = spots.index(None)
            money += rates[k]*cars[i[x]-1]
            spots[k] = i[x]

    else:
        spots[spots.index(abs(i[x]))] = None
        if len(queue) != 0: 
            k = spots.index(None)
            money += rates[k]*cars[queue[0]-1]
            spots[k] = queue[0]
            queue.popleft()

print(money)