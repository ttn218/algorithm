N, M = map(lambda x: int(x), input().split(' '))

def sumMatrix(matrix1, matrix2):
    return [[ c + d for c, d in zip( a, b )] for a, b in zip(matrix1, matrix2)]

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(" ".join(list(map(lambda x: str(x), matrix[i]))))

m1 = []

m2 = []

for _ in range(N):
    m1.append(list(map(lambda x: int(x), input().split(' '))))
    
for i in range(N):
    m2.append(list(map(lambda x: int(x), input().split(' '))))


printMatrix(matrix=sumMatrix(m1,m2))