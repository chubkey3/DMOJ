import math

a = int(input())
b = int(input())

def fraction(a, b):
    l = math.gcd(a, b)
    return a//l, b//l

k = fraction(a%b, b)

if a//b == 0 and a != 0:
    print(f'{k[0]}/{k[1]}')
elif a%b != 0:
    print(a//b, f'{k[0]}/{k[1]}')    
elif a%b == 0:
    print(a//b)