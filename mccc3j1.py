import math

n = int(input())

i = int(input())
j = int(input())

if abs(n-i**2) > abs(n-j**2):
    print(2)
else:
    print(1)