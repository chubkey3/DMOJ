mi = int(input())
ma = int(input())

n = int(input())

location = [0 for x in range(7000)]
motels = [1, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]

for x in range(n):
    a = int(input())
    motels.append(a)
    motels.sort()

location[0] = 1
for x in motels:
    x -= 1
    if x+ma > 6999:
        for y in range(mi, 7000-x):
            if location[x] == 0:
                continue
            if x+y+1 in motels:
                location[x+y] = location[x+y] + location[x]
    else:
        for y in range(mi, ma+1):
            if location[x] == 0:
                continue
            if x+y+1 in motels:
                location[x+y] = location[x+y] + location[x]

print(location[-1])