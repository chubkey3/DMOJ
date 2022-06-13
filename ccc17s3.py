N = int(input())
boards = input().split(" ")
L = [0]*2001
F = [0]*4001

for board in boards:
    L[int(board)] += 1

for i in range(0, len(L) - 1):
    for j in range(i, len(L)):
        if i == j:
            F[i + j] += L[i] // 2
        else:
            F[i + j] += min(L[i], L[j])

highest = 0
combos = 1
for x in range(4001):
    if F[x] > highest:
        highest = F[x]
        combos = 1
    elif F[x] == highest:
        combos += 1

print(highest, combos)