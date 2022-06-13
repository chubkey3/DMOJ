n = int(input())

a = list(input())

for x in range(n-1):
    if int(a[x]) < int(a[x+1]):
        b = a[x+1]
        a[x+1] = a[x]
        a[x] = b
        
        break

print(''.join(a))