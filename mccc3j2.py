n, k = list(map(int, (input().split(" "))))

trail = list(input())
count = 0

for x in trail:
    if x == 'U' and k != 0:
        k -= 1
    elif x == 'D':
        k += 1
        
    if k == 0:
        count += 1
    
print(count)