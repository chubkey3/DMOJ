import sys
inp = sys.stdin.readlines()
matrix = []
dim = int(inp[0].strip('\n'))
row = []
taken = []
no = False
for x in range(len(inp[1:])):
    for y in inp[x+1].strip('\n'):
        for i in y:
            try:
                int(i)
            except ValueError:
                i = ord(i)-55
            if int(i) not in taken:
                row.append(int(i))
                taken.append(int(i))
            else:
                if not no:
                    print('No')
                no = True
                break
    if len(row) == dim:
        matrix.append(row)
        row = []
        taken = []
    else:
        no = True
        break

if not no:
    dups = []

    for x in matrix:
        dups.append(x[0])

    if len(dups) != len(set(dups)) or len(matrix) == dim-1:
        print('No')
    elif matrix[0] == sorted(matrix[0]) and list([x[0] for x in matrix]) == sorted(list([x[0] for x in matrix])):
        print('Reduced')
    else:
        print('Latin')