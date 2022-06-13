i = int(input())
s = input()

if s.count('A') == s.count('B'):
    print('Tie')
elif s.count('A') > s.count('B'):
    print('A')
else:
    print('B')