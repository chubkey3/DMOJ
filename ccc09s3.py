friend = [[],[6],[6],[4,5,6,15],[3,5,6],[3,4,6],[1,2,3,4,5,7],[6,8],[7,9],[8,10,12],[9,11],[10,12],[9,11,13],[12,14,15],[13],[3,13],[17,18],[16,18],[16,17],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

def search(current, end, depth=0, visited=[]):
    depths = []

    if current == end:
        return [depth]

    for x in friend[current]:
        if x not in visited:
            depths += search(x, end, depth + 1, visited + [current])
    
    return depths

while 1:
    a = input()

    if a == 'q':
        break
    
    if a == 'i':
        i1 = int(input())
        i2 = int(input())
        friend[i1].append(i2)
        friend[i2].append(i1)

    elif a == 'd':
        i1 = int(input())
        i2 = int(input())
        friend[i1].remove(i2)
        friend[i2].remove(i1)

    elif a == 'n':
        i1 = int(input())
        print(len(friend[i1]))

    elif a == 'f':
        i1 = int(input())
        c = friend[i1]
        b = []

        for x in c:
            b += friend[x]
        
        b = list(set(b))

        for x in c:
            if x in b:
                b.remove(x)
        
        print(len(b)-1)

    elif a == 's':
        i1 = int(input())
        i2 = int(input())
        f = search(i1, i2)
        if f == []:
            print('Not connected')
        else:
            print(min(f))