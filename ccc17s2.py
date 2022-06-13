a = int(input())

tides = list(map(int, input().split(" ")))

tides = sorted(tides)

if a%2 != 0:
    b = len(tides)//2 + 1
else:
    b = len(tides)//2
    
c = b-1

d = []

for x in range(len(tides)//2):
    if x == len(tides)//2 - 1:
        d += [tides[c], tides[b]]
    else:
        d += [tides[c], tides[b]]
        
    b += 1
    c -= 1

if a%2 != 0:
    d.append(tides[0])

print(*d)