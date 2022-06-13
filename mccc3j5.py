from collections import defaultdict as dd
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

n, m = list(map(int, input().split(' ')))

r = dd(list)

for x in range(m):
    c, d = list(map(int, input().split(' ')))
    r[c].append(d)
    r[d].append(c)

a = [x for x in range(1, n+1)]

b = powerset(a)

answers = []

for c in b:
    k = True
    for x in c:
        if any(elem in c for elem in r[x]):
            k = False
    
    if k:
        answers.append(len(c))

print(max(answers))