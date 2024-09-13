coins = [25, 10, 5, 1]

T = int(input())

for _ in range(T):
    c = int(input())
    
    for coin in coins:
        d = c // coin
        c = c - d * coin
        print( d, end=" ")



