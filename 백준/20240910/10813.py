n, m = map(lambda x: int(x), input().split(' '))

result = [str(x) for x in range(1, n+1)]

for _ in range(m):
    i, j = map(lambda x: int(x) - 1, input().split(' '))
    
    dump = result[i]
    result[i] = result[j]
    result[j] = dump
    
print(' '.join(result))