n, c, v = list(map(int, input().split(' ')))
word = input()

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = list([chr(x) for x in range(97, 123)])

for x in vowels:
    consonants.remove(x)

consonants.remove('y')

countc = 0
countv = 0
outcome = 'YES'

for x in word:
    if x in vowels:
        countc = 0
        countv += 1
    elif x in consonants:
        countv = 0
        countc += 1
    elif x == 'y':
        countv += 1
        countc += 1
    if countv > v:
        outcome = 'NO'
        break
    elif countc > c:
        outcome = 'NO'
        break
print(outcome)