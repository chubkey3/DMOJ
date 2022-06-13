import sys

def f (x):
    return x.strip('\n')

h = ['jack', 'queen', 'king', 'ace']

inp = list(map(f, sys.stdin.readlines()))

p1 = 0
p2 = 0

for x in range(len(inp)):
    if inp[x] == 'ace' and x+4 < len(inp):
        if all([i not in h for i in inp[x+1:x+5]]):
            if x%2 == 0:
                p1 += 4
                print('Player A scores 4 point(s).')
            else:
                p2 += 4
                print('Player B scores 4 point(s).')
    elif inp[x] == 'king' and x+3 < len(inp):
        if all([i not in h for i in inp[x+1:x+4]]):
            if x%2 == 0:
                p1 += 3
                print('Player A scores 3 point(s).')
            else:
                p2 += 3
                print('Player B scores 3 point(s).')
    elif inp[x] == 'queen' and x+2 < len(inp):
        if all([i not in h for i in inp[x+1:x+3]]):
            if x%2 == 0:
                p1 += 2
                print('Player A scores 2 point(s).')
            else:
                p2 += 2
                print('Player B scores 2 point(s).')
    elif inp[x] == 'jack' and x+1 < len(inp):
        if all([i not in h for i in inp[x+1:x+2]]):
            if x%2 == 0:
                p1 += 1
                print('Player A scores 1 point(s).')
            else:
                p2 += 1
                print('Player B scores 1 point(s).')

print(f'Player A: {p1} point(s).')
print(f'Player B: {p2} point(s).')