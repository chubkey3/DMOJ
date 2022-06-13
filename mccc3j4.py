students, rounds = list(map(int, input().split(" ")))

last = {}
targets = {}
temp = {}

for x in range(1, students+1):
    last[x] = 0
    targets[x] = []

k = list(map(int, input().split()))

for x in range(1, students+1):
    targets[x].append(k[x-1])
    temp[x] = []
    
for x in range(rounds):
    for y in targets:
        if targets[y] != []:
            b = targets[y].pop(0)
            temp[b].append(y)
            #targets[b] = sorted(targets[b])
            last[y] = b
    for y in temp:
        targets[y] += sorted(temp[y])
    
    for i in range(1, students+1):
        temp[i] = []


print(*list(last.values()))