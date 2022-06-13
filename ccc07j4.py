import sys

inp = sys.stdin.readlines()

input1 = inp[0].strip('\n')
input2 = inp[1].strip('\n')

values1 = [0 for x in range(26)]
values2 = [0 for x in range(26)]

for x in input1:
    if ord(x) >= 65:
        values1[ord(x)-65] += 1
    
for x in input2:
    if ord(x) >= 65:
        values2[ord(x)-65] += 1
    
if values1 == values2:
    print('Is an anagram.') 
else:
    print('Is not an anagram.')