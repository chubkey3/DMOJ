import sys

inp = sys.stdin.readlines()
n = eval(inp.pop(0))
flows = []
i = []
# # to mark problematic
for x in range(n):
    flows.append(eval(inp.pop(0)))

for x in range(len(inp)):
    i.append(eval(inp[x]))
i.pop(-1)
while len(i) >= 2:
    if i[0] == 99 and len(i) >= 3:
        flows.insert(i[1]-1, flows[i[1]-1]*(i[2]/100))
        flows[i[1]] = flows[i[1]]*(1-(i[2]/100))
        i = i[3:]
    else:
        flows[i[1]-1] = flows[i[1]-1]+flows[i[1]]
        flows.pop(i[1]) 
        i = i[2:]
        

for x in range(len(flows)):
    print(round(flows[x]), end=' ')