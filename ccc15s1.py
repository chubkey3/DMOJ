import sys

inp = sys.stdin.readlines()

k = int(inp.pop(0).strip('\n'))
statements = []

for x in range(k):
    statements.append(int(inp.pop(0).strip('\n')))

x = 0
while 1:
    if x == len(statements):
        break
    if statements[x] == 0:
        statements.pop(x-1)
        statements.pop(x-1)
        x = 0
    else:
        x += 1

print(sum(statements))