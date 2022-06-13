import itertools

t = str(input())
s = str(input())

def cycle(t, i):
    perms = []
    li = list(i)
    for x in range(len(li)):
        li.append(li.pop(0))
        if "".join(li) in t:
            return 'yes'
    return 'no'
    
print(cycle(t,s))