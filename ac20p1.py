import sys

def triangle(a):
    if (a[0]**2+a[1]**2) == a[2]**2:
        return 'R'
    elif (a[0]**2+a[1]**2) >= a[2]**2:
        return 'A'
    elif (a[0]**2+a[1]**2) <= a[2]**2:
        return 'O'

inp = sys.stdin.readlines()

k = eval(inp.pop(0))

for x in range(k):
    print(triangle(sorted(list(map(int, inp.pop(0).strip('\n').split(' '))))))