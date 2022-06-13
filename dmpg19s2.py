keys = []
for x in range(10):
    keys.append(input())
enc = input()

dec = enc[0]

for x in range(1, len(enc)):
    dec += str(keys[int(dec[x-1])].index(enc[x]))

print(dec)