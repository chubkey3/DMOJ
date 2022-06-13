n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())

    maze = []

    for y in range(a):
        maze.append(list(input()))

    dist = [[float('inf') for x in range(b)] for y in range(a)]

    dist[0][0] = 0

    queue = [(0, 0)]

    while queue != []:
        x, y = queue.pop(0)

        m = maze[x][y]

        if m == '+':
            p = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
        elif m == '-':
            p = [[x, y+1], [x, y-1]]
        else:
            p = [[x+1, y], [x-1, y]]
        
        for x2, y2 in p:
            if 0 <= x2 < a and 0 <= y2 < b and maze[x2][y2] != '*':
                if dist[x][y] + 1 < dist[x2][y2]:
                    dist[x2][y2] = dist[x][y] + 1 
                    queue.append((x2, y2))

    if dist[a-1][b-1] == float('inf'):
        print(-1)
    else:
        print(dist[a-1][b-1]+1)