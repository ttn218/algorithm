import sys

K, N = map(int, input().split(' '))

ks = [int(sys.stdin.readline()) for _ in range(K)]

min_length = 1
max_length = 2 ** 31

while max_length - min_length > 1:
    lenth = int((min_length + max_length) / 2)
    count = 0
    for k in ks:
        count += int(k / lenth)
    
    if count >= N:
        min_length = lenth
    else:
        max_length = lenth


print(int((min_length + max_length) / 2))