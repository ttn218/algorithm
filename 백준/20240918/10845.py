N = int(input())

queue = []
for _ in range(N):
    command = input()

    if command.find('push') > -1:
        param = command.split(' ')[1]
        queue.append(int(param))
    
    elif command == 'pop':
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)
    
    elif command == 'size':
        print(len(queue))
        
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    
    elif command == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
    