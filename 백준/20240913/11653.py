N = int(input())


c = 2
while N > 1:
    if N % c == 0:
        N = N / c
        print(c)
    else:
        c += 1
        