N, M = map(int, input().split(' '))

board = [list(input()) for _ in range(N)]

result = []

for y in range(0, N - 7):
    for x in range(0, M - 7):
        count_W = 0
        count_B = 0

        for i in range(y, y+8):
            for j in range(x, x+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        count_W +=1
                    elif board[i][j] != 'B':
                        count_B +=1
                else:
                    if board[i][j] != 'B':
                        count_W +=1
                    elif board[i][j] != 'W':
                        count_B +=1 
        
        result.append(count_W)
        result.append(count_B)
        

print(min(result))