import sys

inp = sys.stdin.readlines()
str1 = inp[0].strip('\n')
str2 = inp[1].strip('\n')
count1 = []
count2 = []
ast = str2.count('*')
newlist = []
for x in range(26):
    count1.append(str1.count(chr(97+x)))


for x in range(26):
    count2.append(str2.count(chr(97+x)))

for x in range(len(count1)):
    newlist.append(count2[x]-count1[x])

if count1 == count2 or (ast == abs(sum(newlist)) and ast > 0 and len(set(list(x > 0 for x in newlist))) == 1):
    print('A')
else:
    print('N')