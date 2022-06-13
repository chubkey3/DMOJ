n, m = list(map(int, input().split(' ')))

dist = [float('inf') for x in range(n)]

dist[0] = 0

pairs = {}

for x in range(m):
    a, b, c = list(map(int, input().split(' ')))

    if a not in pairs:
        pairs[a] = []
    if b not in pairs:
        pairs[b] = []

    pairs[a].append((b, c))
    pairs[b].append((a, c))

queue = [(1, 0)]

while queue != []:
    a = queue.pop(0)

    for p in pairs[a[0]]:
        if dist[a[0]-1]+p[1] < dist[p[0]-1]:
            dist[p[0]-1] = dist[a[0]-1]+p[1]
            queue.append(p)

for x in range(len(dist)):
    if dist[x] == float('inf'):
        print(-1)
    else:
        print(dist[x])