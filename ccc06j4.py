queue = []

seen = []

tasks = {
    1 : [4, 7],
    2 : [1],
    3 : [4, 5],
}

r = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : []
    }

while 1:
    a = int(input())
    b = int(input())

    if a == b and a == 0:
        break
    else:
        if a in tasks:
            tasks[a].append(b)
        else:
            tasks[a] = [b]

for x in tasks.keys():
    for y in tasks[x]:
        r[y].append(x)

for x in r.keys():
    if r[x] == []:
        queue.append(x)

queue_o = queue.copy()

while queue != []:
    a = queue.pop(queue.index(min(queue)))
    seen.append(a)
    if not(a not in tasks and all(y in seen for y in r[a])):
        for x in tasks[a]:
            if r[x] != []:
                if all(y in seen for y in r[x]):
                    queue.append(x)

if len(seen) != 7:
    print('Cannot complete these tasks. Going to bed.')
else:
    print(*seen)