n = int(input())

def test3(b, visited, v):
    a = []
    
    if len(visited) == 4:
        if 0 < b < 25 and b%1 == 0:
            return [int(b)]
        return [0]

    for x in range(4):
        if x in visited:
            continue

        if b != 0:
            a += test3(b*v[x], visited + [x], v)
            a += test3(b/v[x], visited + [x], v)

        a += test3(b+v[x], visited + [x], v)
        a += test3(b-v[x], visited + [x], v)
            

        if len(visited) == 2:
            d = [item for item in [0, 1, 2, 3] if item not in visited]

            l = [v[d[0]]+v[d[1]], v[d[0]]-v[d[1]], v[d[0]]*v[d[1]], v[d[0]]/v[d[1]]]

            for k in l:
                if b+k <= 24 and (b+k)%1 == 0:
                    a += [b+k]
                if b-k <= 24 and (b-k)%1 == 0:
                    a += [b-k]
                if b*k <= 24 and (b*k)%1 == 0:
                    a += [b*k]
                if k != 0 and b/k <= 24 and (b/k)%1 == 0:
                    a += [b/k]
            
    return a 

for x in range(n):
    c = [int(input()), int(input()), int(input()), int(input())]
    print(int(max(test3(0, [], c))))