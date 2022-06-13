n = int(input())

a = 1

while n > a:
    print(a, n, end=" ")
    a += 1
    n -= 1

if n == a:
    print(n)
else:
    print()