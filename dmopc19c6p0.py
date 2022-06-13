a, b, c = map(int, input().strip('\n').split(' '))

if a >= b+c or b >= a+c or c >= a+b:
    print('no')
else:
    print('yes')