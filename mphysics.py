import math

def r(a):
    if len(str(a)) >= 5 and int(str(a)[4]) >= 5:
        return math.ceil(float(a) * 100) / 100.0
    return math.floor(float(a) * 100) / 100.0

n, k = list(map(int, input().split(" ")))

a = n**k
b = 10**(int(math.log10(a)))
a /= b
a = str(r(a))
if len(str(a)) == 4:
    if str(a)[1] != '.':
        print(f'{a[0]}.{a[1]}{a[3]}')
        print(int(math.log10(b))+1)
    else:
        print(a)
        print(int(math.log10(b)))
else:
    print(f'{a}{"0"*(4-len(str(a)))}')
    print(int(math.log10(b)))