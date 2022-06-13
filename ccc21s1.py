n = int(input())

a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

area = 0

for x in range(n):
    area += b[x]*(min(a[x], a[x+1])+(abs(a[x]-a[x+1])/2))
    
print(area)