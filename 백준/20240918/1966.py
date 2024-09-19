T = int(input())

for _ in range(T):
    N, M = map(int, input().split(' '))
    queue = list(map(int, input().split(' ')))
    cursor = M
    count = 0
    while len(queue) > 0:
        if not queue[0] < max(queue):
            count +=1
            queue.pop(0)
            if cursor == 0:
                break
            cursor -= 1
        else:
            if cursor == 0:
                cursor = len(queue) - 1
            else:
                cursor -= 1
            queue.append(queue.pop(0))
    
    print(count)