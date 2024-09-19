import math

def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True


N, M = map(int, input().split(' '))

if N <= 1:
    N = 2

max_target = round(math.sqrt(M))

number_list = set(range(N, M+1))

for i in range(2, max_target+1):
    if isPrime(i):
        primeSet = set(range(i, M+1, i))
        primeSet.remove(i)
        
        number_list -= primeSet

for num in sorted(list(number_list)):
    print(num)