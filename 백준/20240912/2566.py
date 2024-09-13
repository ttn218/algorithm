max_v = -1
x = 0
y = 0

for i in range(1, 10):
    arr = list(map(lambda x: int(x), input().split(' ')))
    arr_max = max(arr)
    max_x = arr.index(arr_max)
    
    if max_v < arr_max:
        max_v = arr_max
        x = max_x + 1
        y = i
        
print(max_v)
print(y, x)
