n, d = list(map(int, input().split(' ')))
t = list(map(int, input().split(' ')))
for x in range(d):
    k = int(input())
    a = t[:k]
    b = t[k:]
    if sum(a) >= sum(b):
        print(sum(a))
        t = t[k:]
    else:
        print(sum(b))
        t = t[:k]