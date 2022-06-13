import math

n = int(input())
height = 0

for x in range(n):
    a, b, c = input().split()
    height += int(a)*float(c)*math.sin(math.radians(int(b)))

print(round(math.sqrt(2*9.8*height)))