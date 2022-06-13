import sys

inp = sys.stdin.readlines()

t = int(inp.pop(0).strip('\n'))

chores = []

for x in range(int(inp.pop(0).strip('\n'))):
    chores.append(int(inp[x].strip('\n')))

chores = sorted(chores)

completed = []

while True:
    if chores[0]+sum(completed) <= t:
        completed.append(chores.pop(0))
    else:
        print(len(completed))
        break