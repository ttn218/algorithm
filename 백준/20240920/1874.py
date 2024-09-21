N = int(input())

stack = []
output = []

i = 1
for _ in range(N):
    n = int(input())
    
    while True:
        if len(stack) == 0 or stack[-1] < n:
            stack.append(i)
            output.append('+')
            i += 1
        elif stack[-1] == n:
            stack.pop()
            output.append('-')
            break
        else:
            print('NO')
            exit()
    
print("\n".join(output))