M = int(input())
N = int(input())

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

min_prime = N + 1
total = 0

for i in range(M, N + 1):
    if isPrime(i):
        total += i
        if min_prime > i:
            min_prime = i

if total > 0:
    print(total)
    print(min_prime)
else:
    print(-1)