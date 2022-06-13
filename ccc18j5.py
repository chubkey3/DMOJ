n = int(input())

paths = {}

for x in range(1, n+1):
    paths[x] = list(map(int, input().split(' ')))[1: ]

stack = [1]
visited = []
distance = [0 for x in range(n)]

distance[0] = 1
ends = []

while stack != []:
    a = stack.pop(0)
    if a not in visited:
        if paths[a] == []:
            visited += [a]
            ends.append(a)
            continue
        else:
            stack += paths[a]
            f = distance[a-1]
            for x in paths[a]:
                if distance[x-1] != 0:
                    distance[x-1] = min(f+1, distance[x-1])
                else:
                    distance[x-1] = f+1
        visited.append(a)

if len(visited) == n:
    print('Y')
else:
    print('N')

print(min([distance[x-1] for x in ends]))