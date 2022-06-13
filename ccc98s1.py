def censor(n, t):
    text = []
    censored = []
    for x in range(n):
        text.append(t[x].split(' '))
        c = []
        for i in range(len(text[-1])):
            if len(text[x][i]) == 4:
                c.append(i)
        censored.append(c)
    for x in range(len(censored)):
        for y in censored[x]:
            text[x][y] = '****'
    for x in range(len(text)):
        for y in range(len(text[x])):
            print(text[x][y], end=' ')
        print()
    
import sys

inp = sys.stdin.readlines()

for x in range(len(inp[1:])):
    inp[x+1] = inp[x+1][:-1]

censor(int(inp[0].strip('\n')), inp[1:])

#['The quick brown fox jumps over the lazy dog', 'Now is the time for all good people to come to the aid of the party']