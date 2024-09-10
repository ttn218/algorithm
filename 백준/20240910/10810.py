n, m = map(lambda x: int(x), input().split(' '))

x = ['0' for x in range(n)]

for i in range(m):
    start, end, num = map(lambda x: int(x), input().split(' '))
    
    x[start-1:end] = [f'{num}' for x in range(start-1, end)]
    
print(" ".join(x))