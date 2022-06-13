import sys, itertools

def search(current, end, visited, depth=0):
    a = []

    b = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

    if current == end or depth == 6:
        return [[visited for visited,_ in itertools.groupby(visited)]]

    for x in b:
        k = current[0]+x[0]
        l = current[1]+x[1]
        if 1 <= k <= 8 and 1 <= l <= 8 and [k, l] not in visited:
            a += search([k, l], end, visited + [current], depth+1)

    return a

start = list(map(int, input().split(' ')))
end = list(map(int, input().split(' ')))

m = 7

for x in search(start, end, []):
    if len(x) < m:
        m = len(x)

print(m)