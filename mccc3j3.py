import sys

def precompute(s, t):
    k = 0
    for x in range(65, 65+26):
        k += s.count(chr(x))*t.count(chr(x))

    return k

g = input()

c = set()

a = sys.stdin.readline().strip('\n')
b = sys.stdin.readline().strip('\n')

d = precompute(a, b)

o2 = {}

for x in range(65, 65+26):
    o2[chr(x)] = a.count(chr(x))

for x in set(b):
    for y in set(a):    
        c.add(d + o2[y] - o2[x])

print(max(c))