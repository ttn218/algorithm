N = int(input())

canvas = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    x, y = map(lambda x: int(x), input().split(' '))
    
    paper = [1,1,1,1,1,1,1,1,1,1]
    
    for i in range(10):
        canvas[x+i][y:y+10] = paper

def sumMatrix(matrix):
    total = 0
    for i in range(len(matrix)):
        total += sum(matrix[i])
    
    return total

print(sumMatrix(canvas))
