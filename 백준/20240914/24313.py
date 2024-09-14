a1, a0 = map(int, input().split(' '))
c = int(input())
n0 = int(input())

result = 1
if (c - a1) < 0:
    result = 0
if n0*(c-a1) < a0:
    result = 0
    
print(result)