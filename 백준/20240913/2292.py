N = int(input())

c = 1
while N > 1:
    N = N - (c * 6)
    c = c + 1
    
print(c)