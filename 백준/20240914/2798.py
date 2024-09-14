N, M = map(int, input().split(' '))

cards = list(map(int, input().split(' ')))

max_s = -1

for i in range(0, N - 2):
    for j in range(i+1, N - 1):
        for k in range(j+1, N):
            s = cards[i] + cards[j] + cards[k]
            
            if s > max_s and s <= M:
                max_s = s
                
print(max_s)