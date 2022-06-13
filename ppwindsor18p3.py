n = int(input())

rows = [
    'qwertyuiop',
    'asdfghjkl',
    'zxcvbnm']

c = [0 for x in range(n)]

for x in range(n):
    a = input()
    for y in rows:
        if all(k in y for k in a):
            c[x] = 1

print(c.count(1))