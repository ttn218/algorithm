def solution(board):
    answer = 0
    safeMap = [[1 for c in i] for i in board]
    
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 1:
                safeMap[i][j] = 0
                
                im = i - 1 if i - 1 >= 0 else 0
                ip = i + 1 if i + 1 < len(board) else len(board) - 1
                jm = j - 1 if j - 1 >= 0 else 0
                jp = j + 1 if j + 1 < len(row) else len(row) - 1
                
                safeMap[i][jm] = 0
                safeMap[i][jp] = 0
                safeMap[im][j] = 0
                safeMap[ip][j] = 0
                safeMap[im][jm] = 0
                safeMap[im][jp] = 0
                safeMap[ip][jp] = 0
                safeMap[ip][jm] = 0
    
    
    for row in safeMap:
        for col in row:
            answer += col
    
    return answer