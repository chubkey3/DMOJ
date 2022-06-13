n, h = list(map(int, input().split(' ')))

grid = []
dist = []

for x in range(n):
    grid.append(list(map(int, input().split(' '))))
    dist.append([float('inf') for x in range(n)])

queue = [(0,0)] 
dist[0][0] = 0

while queue != []:
    x, y = queue.pop(0)

    b = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    for x2, y2 in b:
        if 0 <= x2 < n and 0 <= y2 < n and dist[x][y]+1 < dist[x2][y2] and abs(grid[x][y]-grid[x2][y2]) <= h:
            dist[x2][y2] = dist[x][y] + 1
            queue.append((x2, y2))


if dist[n-1][n-1] != float('inf'):
    print('yes')
else:
    print('no')