N, K = map(int, input().split(' '))


c = 0
t = 0
for i in range(1, N+1):
    if N % i == 0:
        c += 1
        t = i
        
        if c == K:
            break

if c < K:
    t = 0

print(t)