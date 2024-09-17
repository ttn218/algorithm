import sys

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

def bubbleSort(iterable, desc = False):
    c_iter = [x for x in iterable]
    
    dir_fc = lambda x, y: x < y if desc else x > y
    
    for _ in range(len(c_iter)):
        for j in range(len(c_iter)-1):
            if dir_fc(c_iter[j], c_iter[j + 1]):
                temp = c_iter[j]
                c_iter[j] = c_iter[j + 1]
                c_iter[j + 1] = temp
    return c_iter

def merge(list_1:list, list_2:list, desc=False):
    sorted_list = []
    index_1 = 0
    index_2 = 0

    while index_1 < len(list_1) and index_2 < len(list_2):
        
        if desc:
            if list_1[index_1] >= list_2[index_2]:
                sorted_list.append(list_1[index_1])
                index_1 += 1
            else:
                sorted_list.append(list_2[index_2])
                index_2 += 1
        else:
            if list_1[index_1] <= list_2[index_2]:
                sorted_list.append(list_1[index_1])
                index_1 += 1
            else:
                sorted_list.append(list_2[index_2])
                index_2 += 1
            
    if index_1 < len(list_1):
        sorted_list += list_1[index_1:]
    else:
        sorted_list += list_2[index_2:]

    return sorted_list

def mergeSort(iterable, desc=False):
    len_iter = len(iterable)
    
    if len_iter >= 2:
        return merge(mergeSort(iterable[0: len_iter//2], desc), mergeSort(iterable[len_iter//2:], desc), desc)
    
    return iterable

# 빠른 입력
sys.stdin.readline()

def counting_sort(iterable:list, desc=False):
    counts = {}

    for x in iterable:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
        
    result = []

    if desc:
        for num in range(max(iterable) + 1, 0, -1):
            while num in counts and counts[num] != 0:
                result.append(num)
                counts[num] -= 1
    else:
        for num in range(max(iterable) + 1):
            while num in counts and counts[num] != 0:
                result.append(num)
                counts[num] -= 1
    return result


def isMate(word1, word2):
    if word1 == '(' and word2 == ')':
        return True
    if word1 == '[' and word2 == ']':
        return True
    return False