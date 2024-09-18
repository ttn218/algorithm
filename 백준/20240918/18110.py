import sys
N = int(input())

def real_round(number):
    target = int((number - int(number)) * 10)
    
    if target >= 5:
        return int(number) + 1

    return int(number)

if N == 0:
    print(0)
else:
    opinions = sorted([int(sys.stdin.readline()) for _ in range(N)])
    cut_count = real_round((N * 0.15))
    
    total = 0
    for i in range(cut_count, N - cut_count):
        total += opinions[i]

    print(real_round(total / (N - cut_count * 2)))