inp = input()
right = 'pusheen'
wrong = 0
for x in range(len(inp)):
    if inp[x] != right[x]:
        wrong += 1
print(wrong)