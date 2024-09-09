import math

n = int(input())

result = 'int'

for i in range(math.ceil(n/4)):
    result = 'long ' + result


print(result)