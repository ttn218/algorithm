t = int(input())

for _ in range(t):
    l, w = input().split(' ')
    
    l = int(l)
    
    p = ''
    
    for c in w:
        p += c*l
        
    print(p)
    