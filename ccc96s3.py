def generator(l, i, m, k):
    if i.count('1') > k:
        return ''
    elif l == m and i.count('1') != k:
        return ''
    elif l == m:
        return f'{i} '
    l += 1
    return generator(l, i+'0', m, k)+generator(l, i+'1', m, k)

n = int(input())
for l in range(n):
    a, b = input().split(' ')
    print('The bit patterns are')
    patterns = generator(0, '', int(a), int(b)).split(' ')
    patterns.reverse()
    for x in patterns:
        if x != '':
            print(x)