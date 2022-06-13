import sys

#inp = sys.stdin.readlines()
w = int(input())
position = 0
#+2 - 2 1 
#2 + (2-1)
#2 2 1 - +
3 - (2+1) - 9
#3 (2+1) - 9 -
#3 - (2+1) 9 -
3 - (2+1) - 9
string = 'WELCOME TO CCC GOOD LUCK TODAY'.split(' ')
strings = []
line = ''
for x in range(len(string)):
    #print(len(line), len(string[x]))
    if len(string[x])+len(line) > w:
        strings.append(line)
        line = string[x]+' '
    elif len(string[x])+len(line):
        line += string[x]+' '

if len(string) > 1:
    strings.append(line)
#for x in range(len(strings)):
    #strings[x] = strings[x].split(' ')       
for x in range(len(strings)):
    dots = w-(len(strings[x])-list(strings[x]).count(' '))
    strings[x] = strings[x].split(' ')[:-1]
    #for y in range(dots):
    #strings[x][len(strings[x])%(x+1)] += '.'
    i = 0
    while dots > 0:
        #print(i)
        if i == len(strings[x]) or i == len(strings[x])-1:
            i = 0
        strings[x][i] += '.'
        dots -= 1
        i += 1
'''
for x in range(len(string)):
    if len(string[x])+position == w:
        print(string[x])
        position += w
    elif len(string[x])+position < w:
        print(string[x], end='')
        position += len(string[x])
    else:
        print((w-position%w) * '.', end='')
        print()
'''

for x in range(len(strings)):
    print(''.join(strings[x]))