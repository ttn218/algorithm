

store = {}

def makeOne(n):
    global store
    
    if n in store:        
        return store[n]

    if n == 1:
        return 0
    
    case1 = makeOne(n-1) + 1
    
    if n % 3 == 0 and n % 2 == 0:
        case2 = makeOne(n // 3) + 1
        case3 = makeOne(n // 2) + 1
        minCase = min(case1, case2, case3)
        
        store[n] = minCase

        return minCase
    elif n % 3 == 0:
        case2 = makeOne(n // 3) + 1
        minCase = min(case1, case2)
        store[n] = minCase
        
        return minCase
    elif n % 2 == 0:
        case2 = makeOne(n // 2) + 1
        minCase = min(case1, case2)
        store[n] = minCase
        
        return minCase
    
    store[n] = case1
    
    return case1

N = int(input())

for i in range(1, N + 1):
    c = makeOne(i)
    
    if i == N: 
        print(c)