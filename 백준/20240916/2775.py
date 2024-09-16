T = int(input())

apart = {}

def fun(n, i):
    if f'{n}-{i}' in apart:
        return apart[f'{n}-{i}']
    
    if n > 0:
        total = 0
        for x in range(i):
            total += fun(n-1, i - x)
            
        apart[f'{n}-{i}'] = total
        return total
    
    apart[f'0-{i}'] = i
    return i

for _ in range(T):
    k = int(input())
    n = int(input())
    
    print(fun(k, n))