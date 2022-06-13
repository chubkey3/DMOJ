def maxdist(current, nodes, visited, b):
    l = []
    if nodes[current] == []:
        return [b]
    
    for x in nodes[current]:
        l += maxdist(x, nodes, visited + [current], b+1)

    return l

def filldict(d):
    for x in d.copy():
        for y in d.copy()[x]:
            if y not in d.keys():
                d[y] = []
    
    return d

n = int(input())

for x in range(n):
    nodes = {}
    c = int(input())
    k = []
    for i in range(c):
        k.append(input())
    name = k[-1]
    seen = [k[-1]]
    current = name
    for y in range(c):
        name = k[y]
        
        if name not in seen:
            seen.append(name)

            if current not in nodes:
                nodes[current] = []

            nodes[current] += [name]
        
        
        current = name

    print(10*c - max(maxdist(seen[0], filldict(nodes), [], 0))*20)