N = int(input())

min_c = N

for i in range(int(N/2), N):
    t = i + sum([int(x) for x in str(i)])
    
    if t == N and min_c > i:
        min_c = i

if min_c == N:
    min_c = 0

print(min_c)