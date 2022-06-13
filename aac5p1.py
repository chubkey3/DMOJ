n = int(input())

b = list(map(int, input().split(" ")))

e = 0
o = 0

for x in b:
    if x%2 == 0:
        e += 1
    else:
        o += 1

print(o//2+e//2)