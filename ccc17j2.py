import sys
inp = sys.stdin.readlines()
n = inp[0].strip('\n')
k = inp[1].strip('\n')
s = 0
for x in range(int(k)+1):
    s += int(n)
    n = str(n) + '0'
print(s)