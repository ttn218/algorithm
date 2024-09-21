N = int(input())

times = sorted(list(map(int, input().split(' '))))

total = 0

acc = 0 
for time in times:
    total += acc + time
    acc += time
    
print(total)