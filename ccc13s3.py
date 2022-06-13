team = int(input())
games_played = int(input())

def search(g, t):
    l = []

    if g == []:
        return list(t.values())

    tc = t.copy()

    tc[g[0][0]] += 3

    l += search(g[1: ], tc)

    tc = t.copy()

    tc[g[0][1]] += 3

    l += search(g[1: ], tc)

    tc = t.copy()

    tc[g[0][0]] += 1
    tc[g[0][1]] += 1
        
    l += search(g[1: ], tc)

    return l

teams = {1: 0, 2: 0, 3: 0, 4: 0}
played = {1: [2,3,4], 2: [1,3,4], 3:[1,2,4], 4:[1,2,3]}

for x in range(games_played):
    a = list(map(int, input().split(' ')))
    if a[3] > a[2]:
        teams[a[1]] += 3
    elif a[2] > a[3]:
        teams[a[0]] += 3
    elif a[2] == a[3]:
        teams[a[0]] += 1
        teams[a[1]] += 1
    
    played[a[0]].remove(a[1])
    played[a[1]].remove(a[0])

games = []

for x in range(1, 5):
    while played[x] != []:
        c = played[x].pop()
        for y in range(1, 5):
            if y == x:
                continue
            if x in played[y]:
                games.append([x, y])
                played[y].remove(x)

t = search(games, teams)

count = 0

for x in range(0, len(t), 4):
    k = [t[i] for i in range(x, x+4)]
    if k.index(max(k)) == team-1 and k.count(max(k)) == 1:
        count += 1

print(count)