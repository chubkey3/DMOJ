import sys

b = int(input())

r = int(input())
c = int(input())

floor = []

for x in range(r):
    floor.append(list(input()))

visited = []

rooms = []

for x in range(r):
    for y in range(c):
        if floor[x][y] != 'I' and [x, y] not in visited:
            stack = [[x, y]]
            k = []

            if [x, y] not in visited:

                while stack != []:
                    a = stack.pop(0)
                    x2 = a[0]
                    y2 = a[1]
                    if floor[x2][y2] != 'I':
                        d = [[x2+1, y2], [x2-1, y2], [x2, y2+1], [x2, y2-1]]
                        for l in d:
                            if l not in visited and 0 <= l[0] <= r-1 and 0 <= l[1] <= c-1:
                                stack.append(l)

                        if [x2, y2] not in visited:
                            visited.append([x2, y2])
                            k.append([x2, y2])

                rooms.append(k)
                k = []

rooms = sorted(list(map(lambda x: len(x), rooms)), reverse=True)
l = rooms.copy()
i = 0

while b != 0:
    if i == len(rooms):
        if i == 1:
            print(f'{i} room, {b} square metre(s) left over')
        else:
            print(f'{i} rooms, {b} square metre(s) left over')
        sys.exit()
    elif rooms[i] == 0:
        i += 1
    else:
        rooms[i] -= 1
        b -= 1

if b == 0 and len(set(rooms)) == 1:
    print(f'{len(rooms)} rooms, 0 square metre(s) left over')
elif i == 1:
    print(f'{i} room, {l[i]-rooms[i]} square metre(s) left over')
else:    
    print(f'{i} rooms, {l[i]-rooms[i]} square metre(s) left over')