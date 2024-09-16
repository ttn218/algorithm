import sys
N = int(input())
count = [0] * 10001

for _ in range(N):
    n = int(sys.stdin.readline())    
    count[n] += 1

for num in range(10001):
    while count[num] != 0:
        count[num] -= 1
        print(num)
