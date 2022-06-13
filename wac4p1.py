n, q = list(map(int, input().split(' ')))

a = list(map(int, input().split(' ')))

for x in range(q):
    i = list(map(int, input().split(' ')))
    if i[0] == 1:
        a[i[1]-1:i[2]] = sorted(a[i[1]-1:i[2]])
    else:
        a[i[1]-1:i[2]] = sorted(a[i[1]-1:i[2]], reverse=True)

for x in range(len(a)):
    if x == len(a)-1:
        print(a[x])
    else:
        print(a[x], end=' ')