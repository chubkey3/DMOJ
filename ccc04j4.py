whitelist = list(chr(x) for x in range(65, 91))

input1 = input()
input2 = list(input())

keyword_len = len(input1)

blocked = [[] for x in range(keyword_len)]
input2 = ''.join(filter(whitelist.__contains__, input2))

for x in range(len(input2)):
    blocked[x%keyword_len].append(input2[x])

for x in range(keyword_len):
    shift = ord(input1[x].upper())-65
    for i in range(len(blocked[x])):
        newchar = ord(blocked[x][i])+shift
        if newchar > 90:
            newchar = newchar-26
        blocked[x][i] = chr(newchar)

for x in range(len(blocked[-1])):
    for y in range(len(blocked)):
        #print(blocked, x, y)
        if ord(blocked[y][x]) >= 65:
            print(blocked[y][x], end='')

for x in range(len(blocked)):
    if len(blocked[x]) > len(blocked[-1]):
        print(blocked[x][-1], end='')