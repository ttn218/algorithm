N, K = map(int, input().split(' '))

coins = [int(input()) for _ in range(N)]

count = 0

for i in range(N - 1, -1, -1):
    coin = coins[i]
    
    count += K // coin
    K = K % coin
    
    if K == 0:
        break

print(count)