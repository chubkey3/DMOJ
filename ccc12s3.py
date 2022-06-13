def findlargestdif(x, i=0):
    if i == 0:
        return abs(min(x)-max(x))
    else:
        if abs(max(x)+1-i) > abs(min(x)+1-i):
            return abs(max(x)+1-i)
        else:
            return abs(min(x)+1-i)
            
n = int(input())

o = [0 for x in range(1000)]

for x in range(n):
    o[int(input())-1] += 1

m = max(o)
index1 = [i for i, x in enumerate(o) if x == m]

oc = o.copy()
while m in oc:
    oc.remove(m)
m = max(oc)

index2 = [i for i, x in enumerate(o) if x == m]

if len(index1) == 1 and len(index2) == 1:
    print(abs(index1[0]-index2[0]))
elif len(index1) > 1:
    print(findlargestdif(index1))
else:
    print(findlargestdif(index2, int(index1[0])+1))