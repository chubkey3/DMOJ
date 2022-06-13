#Input
graph1 = {'A': [],
         'B': [],
         'C': [],
         'D': [],
         'E': [],
         'F': [],
         'G': [],
         'H': [],
         'I': [],
         'J': [],
         'K': [],
         'M': [],
         'O': [],
         'P': [],
         'Q': [],
         'R': [],
         'S': [],
         'T': [],
         'U': [],
         'V': [],
         'W': [],
         'X': [],
         'Y': [],
         'Z': []
}

reverse = []

isDone = False
while isDone == False:
  temp = input()
  temp1 = temp[::-1]
  if temp == "**":
    isDone = True
  else: 
    reverse.append(temp)
    for key in graph1:
      if temp[0] == key:
        graph1[key] = graph1[key] + list(temp[1])
      if temp1[0] == key:
        graph1[key] = graph1[key] + list(temp1[1])

def find_paths(current, end, visited):
    k = []

    if current == end:
        return [visited]

    for x in graph1[current]:
        if f'{current}{x}' not in visited and f'{x}{current}' not in visited:
            k += find_paths(x, end, visited+[f'{current}{x}'])

    return k

cum = {}

for x in reverse:
    cum[x] = 0
    cum[x[::-1]] = 0

paths = find_paths('A', 'B', [])

for x in paths:
    for y in x:
        cum[y] += 1

c = len(paths)
answer = []

for x in cum:
    if cum[x] == c:
        answer.append(x)

for x in answer:
    if x in reverse:
        print(x)
    else:
        print(x[::-1])

print(f'There are {len(answer)} disconnecting roads.')