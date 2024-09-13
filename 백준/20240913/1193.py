N = int(input())


l = 1
while N > l:
    N -= l
    l += 1

if l % 2 == 0:
    c, p = 1, l
    while N > 1:
        c += 1
        p -= 1
        N -= 1
        
else:
    c, p = l, 1
    while N > 1:
        c -= 1
        p += 1
        N -= 1


print(f'{c}/{p}')