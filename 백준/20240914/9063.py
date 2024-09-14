N = int(input())

max_x = -10001
max_y = -10001
min_x = 10001
min_y = 10001

for _ in range(N):
    x, y = map(int, input().split(' '))
    
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y
        
print(f'{(max_x - min_x)*(max_y-min_y)}')