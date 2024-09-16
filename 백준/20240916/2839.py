N = int(input())

count_5 = N // 5
mod_5 = N % 5

count_3 = -1
mod_3 = -1

for i in range(0, count_5+1):
    target = mod_5 + 5 * i
    
    count_3 = target // 3
    mod_3 = target % 3
    
    if mod_3 == 0:
        count_5 -= i
        break

if mod_3 > 0:
    print(-1)
else:
    print(count_5+count_3)