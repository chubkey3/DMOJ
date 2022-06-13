i = list(input())

grid = [1,2,3,4]

for x in i:
    if x == 'H':
        grid = grid[2: ]+grid[:2]
    else:
        grid.insert(0, grid.pop(1))
        grid.insert(-1, grid.pop(3))

print(grid[0], grid[1])
print(grid[2], grid[3])