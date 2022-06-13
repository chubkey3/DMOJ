import sys

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