q = int(input())

n = int(input())

d = sorted(list(map(int, input().split(' '))))
p = sorted(list(map(int, input().split(' '))))

if q == 1:
    print(sum([max(d[x], p[x]) for x in range(n-1, -1, -1)]))

elif q == 2:
    print(sum([max(d[x], p[n-x-1]) for x in range(n-1, -1, -1)]))