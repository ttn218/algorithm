def facto(n):
    if n == 0: return 1
    
    if n > 2:
        return n * facto(n-1)
    
    return n

N = int(input())

print(facto(N))