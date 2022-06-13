a, b = list(map(int, input().split(' ')))

n = int(input())

grid = [[0 for x in range(b)] for y in range(a)]

cats = []

for x in range(n):
    i1, i2 = list(map(int, input().split(' ')))
    cats.append([i1-1, i2-1])

stack = [[1, 0], [0, 1]]
grid[0][0] = 1
i = 0
v = []
while stack != []:
    c1 = stack[0][0]
    c2 = stack[0][1]

    if 0 <= c1 < len(grid) and 0 <= c2 < len(grid[0]) and [c1, c2] not in cats and [c1, c2] not in v:
        if c1 == 0:
            grid[c1][c2] = grid[c1][c2-1]
        elif c2 == 0:
            grid[c1][c2] = grid[c1-1][c2]
        else:
            grid[c1][c2] = grid[c1-1][c2]+grid[c1][c2-1]

        stack.append([c1+1, c2])
        stack.append([c1, c2+1])

    v.append(stack.pop(0))

print(grid[a-1][b-1])