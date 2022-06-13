import sys

inp = sys.stdin.readlines()

n = eval(inp.pop(0))

pa = list(inp.pop(0).strip('\n').split(' '))
pb = list(inp.pop(0).strip('\n').split(' '))

partners = {}

for x in range(n):
    partners[pa[x]] = pb[x]

keys = list(partners.keys())

out = True

for x in range(n):
    if partners[keys[x]] == keys[x] or keys[x] != partners[partners[keys[x]]]:
        print('bad')
        out = False
        break

if out:
    print('good')