import sys

n = int(sys.stdin.readline())

trees = [0 for x in range(n)]

trees[0] = int(sys.stdin.readline())

for x in range(1, n):
    trees[x] = trees[x-1]+int(sys.stdin.readline())

q = int(sys.stdin.readline())

for x in range(q):
    i = sys.stdin.readline().split(" ")
    i1 = int(i[0])
    i2 = int(i[1])
    if i1 == 0:
        print(trees[i2])
    else:
        print(trees[i2]-trees[i1-1])