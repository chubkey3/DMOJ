vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def convert(i):
    if i[-2: ] == 'or' and i[-3] not in vowels and len(i) > 4:
        return i.replace('or', 'our')   
    else:
        return i

while True:
    inp = input()
    if inp == 'quit!':
        break
    print(convert(inp))