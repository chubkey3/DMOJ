m = int(input())
n = int(input())
k = int(input())

rows = [0 for x in range(m)]
cols = [0 for x in range(n)]
count = 0

for x in range(k):
    a = input().split(' ')
    b = a[0]
    c = int(a[1])-1
    if b == 'R':
        rows[c] += 1
    else:
        cols[c] += 1

for x in range(len(rows)):
    for y in range(len(cols)):
        if (rows[x]+cols[y]) % 2 != 0:
            count += 1

print(count)