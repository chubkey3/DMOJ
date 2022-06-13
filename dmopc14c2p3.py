import sys

n = int(input())
e = sorted(map(int, sys.stdin.readline().strip('\n').split(' ')))
d = sorted(map(int, sys.stdin.readline().strip('\n').split(' ')), reverse=True)

print(sum([e[x]*d[x] for x in range(n)]))