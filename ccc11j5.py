from itertools import combinations

def search(friend, d):
    #print(friend, d)
    return d[friend]
    
def get_combs(k):
    a = [x for x in range(1, k+1)]
    
    b = []

    for x in range(2, k+1):
        b += list(map(list, list(combinations(a, x))))
    
    return b
    
n = int(input())

friends = {}

for x in range(1, n+1):
    friends[x] = []

for x in range(1, n):
    friends[int(input())].append(x)

a = get_combs(n-1)

for x in range(1, n):
    a.append([x])

a.append([])

for x in range(len(a)):
    g = True
    while g:
        g = False
        for y in range(len(a[x])):
            k = search(a[x][y], friends)
            for z in k:
                if z not in a[x]:
                    a[x] += [z]
                    g = True

seen = []
count = 0

for x in a:
    if sorted(x) in seen:
        continue
    else:
        seen.append(sorted(x))
        count += 1

print(count)