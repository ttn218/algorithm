n, m = map(lambda x: int(x), input().split(' '))

s = [str(x) for x in range(1, n+1)]

for _ in range(m):
    i, j = map(lambda x: int(x) - 1, input().split(' '))
    
    ns = s[i:j + 1]
    ns.reverse()
    s[i:j + 1] = ns
    
    
print(" ".join(s))