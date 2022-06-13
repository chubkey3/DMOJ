n = int(input())

sunflowers = []

for x in range(n):
    sunflowers.append(list(map(int, input().split(' '))))

a = [x[0] for x in sunflowers]

if a == sorted(a) and sunflowers[0] == sorted(sunflowers[0]):
    for x in sunflowers:
        print(*x)
elif a == sorted(a) and sunflowers[0] == sorted(sunflowers[0], reverse=True):
    for x in range(n-1, -1, -1):
        print(*[sunflowers[y][x] for y in range(n)])
elif a == sorted(a, reverse=True) and sunflowers[0] == sorted(sunflowers[0]):
    for x in range(n):
        print(*[sunflowers[y][x] for y in range(n-1, -1, -1)])
else:
    for x in range(n-1, -1, -1):
        print(*sunflowers[x][::-1])