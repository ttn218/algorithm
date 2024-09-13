
def getmeasures(num):
    result = []
    
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            result.append(i)
            
    return result

while True:
    N = int(input())
    
    if N == -1:
        break
    
    measures = getmeasures(N)
    
    if sum(measures) == N:
        print(f'{N} = {" + ".join(map(str, measures))}')
    else:
        print(f'{N} is NOT perfect.')
        
