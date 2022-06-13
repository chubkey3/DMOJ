for x in range(5):
    k = [float('inf') for i in range(101)]
    k[1] = 0
    currencies = []
    m = int(input())
    n = int(input())

    for y in range(n):
        currencies.append(int(input()))
    
    for i in range(1, len(k)):
        if k[i] == float('inf'):
            continue
        for l in currencies:
            if i+l < len(k):
                k[i+l] = min(k[i]+1, k[i+l])
        
    print(k[m+1])