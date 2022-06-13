n = int(input())

for x in range(n):

    d = int(input())

    grid = []

    for x in range(d):
        row = []
        for y in range(d):
            row.append(int(input()))
        
        grid.append(row)
        row = []

    dist = [[float('inf') for x in range(d)] for y in range(d)]

    dist[0][0] = 0

    m = grid[0][0]

    queue = [(0, 0)]

    while queue != []:
        x, y = queue.pop(0)

        b = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        for x2, y2 in b:
            if 0 <= x2 < d and 0 <= y2 < d and abs(grid[x2][y2]-grid[x][y]) <= 2:
                if grid[x2][y2] > m or grid[x][y] > m:
                    p = 1
                else:
                    p = 0
                if dist[x][y]+p < dist[x2][y2]:
                    dist[x2][y2] = dist[x][y]+p
                    queue.append((x2, y2))

    k = dist[d-1][d-1]

    if k != float('inf'):
        print(k)
    else:
        print('CANNOT MAKE THE TRIP')
    
    print()