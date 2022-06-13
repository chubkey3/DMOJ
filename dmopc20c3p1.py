import sys
inp = sys.stdin.readlines()

killmeinstantly = list(map(int, inp.pop(1).strip('\n').split(' ')))

if len(killmeinstantly) == int(inp.pop(0).strip('\n')) and len(killmeinstantly) == len(set(killmeinstantly)):
    print('YES')
else:
    print('NO')