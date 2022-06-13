import sys

sys.setrecursionlimit(10010)

n = int(input())

students = {}

def nuts(depth, dic, current, target):
    if depth == n:
        return -1
    if current not in dic:
        return -1
    if dic[current] == target:
        return depth

    return nuts(depth+1, dic, dic[current], target)

for i in range(n):
    s, f = input().split()
    students[s] = f

while 1:
    a, b = input().split()
    if a == b and a == '0':
        break
    d = nuts(0, students, a, b)
    if d == -1:
        print('No')
    else:
        print('Yes', d)