import sys
'''
ang1 = int(input())
ang2 = int(input())
ang3 = int(input())

if ang1+ang2+ang3 != 180:
    print('Error')
elif len(set([ang1, ang2, ang3])) == 1:
    print('Equilateral')
elif len(set([ang1, ang2, ang3])) == 2:
    print('Isosceles') 
else:
    print('Scalene')

'''
inp = sys.stdin.readlines()

ant = 0
dav = 0

for x in range(int(inp.pop(0).strip('\n'))):
    r = list(map(int, inp.pop(0).strip('\n').split(' ')))
    if r[0] == r[1]:
        continue
    elif r[0] > r[1]:
        dav += r[0]
    else:
        ant += r[1]

print(100-ant)
print(100-dav)