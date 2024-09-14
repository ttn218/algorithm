def plusMatrix(matrix1, matrix2):
    return [[ c + d for c, d in zip( a, b )] for a, b in zip(matrix1, matrix2)]

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(" ".join(list(map(lambda x: str(x), matrix[i]))))
        
def sumMatrix(matrix):
    total = 0
    for i in range(len(matrix)):
        total += sum(matrix[i])
    
    return total

def basetransfor(n, b):
    result = ''
    
    while n > 0:
        n, mod = divmod(n, b)
        
        if mod >= 10:
            result += chr(mod+55)
        else:
            result += str(mod)
    
    return result[::-1]

def getmeasures(num):
    result = []
    
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            result.append(i)
            
    return result

def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num/2) + 1, 2):
        if num % i == 0:
            return False
    
    return True       