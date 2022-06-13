import sys

word = input()

vowels = ['a','e','i','o','u']
letters = [chr(x) for x in range(97,123)]
newword = ''

for char in range(len(word)):
    distance = []
    n = letters.index(word[char])
    if word[char] not in vowels:
        if word[char] == 'z':
            n = 25
        else:
            n += 1
            
            while letters[n] in vowels:
                n +=1
        for i in list([letters.index(x) for x in vowels]):
            distance.append(letters.index(word[char])-i)
        for x in sorted(map(abs,distance)):
            if letters[letters.index(word[char])-x] in vowels:
                s = letters[letters.index(word[char])-x]
            else:
                s = letters[letters.index(word[char])+x]
            break
        closestvow = min([letters.index(x) for x in vowels], key=lambda x: abs(x-letters.index(word[char])))
        newword += f'{word[char]}{s}{letters[n]}'
    else:
        newword += word[char]

print(newword)