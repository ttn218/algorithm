N = int(input())

num_list = list(map(int, input().split(' ')))

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

c = 0
for num in num_list:
    if isPrime(num):
        c += 1
        
print(c)