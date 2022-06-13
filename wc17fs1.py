import sys

n = int(sys.stdin.readline())

k = []

a = list(map(int, input().split(" ")))
a.sort()
b = list(map(int, input().split(" ")))
b.sort()

for x in range(n):
    k.append(abs(a[x]-b[x]))

print(max(k))