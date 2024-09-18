N = int(input())

stack = []
for _ in range(N):
    command = input()

    if command.find('push') > -1:
        param = command.split(' ')[1]
        stack.append(int(param))
    
    elif command == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    
    elif command == 'size':
        print(len(stack))
        
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif command == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    