T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split(' '))
    
    y = ((N-1) % H) + 1
    x = (N-1) // H + 1
    
    print(y*100 + x)
    