import sys
inp = sys.stdin.readlines()
input1 = int(inp[0].strip('\n'))
input2 = int(inp[1].strip('\n'))
if input1 == input2:
    pass
elif input1 > input2:
    print('CS452')
else:
    print('PHIL145')