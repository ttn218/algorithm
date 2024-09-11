n = int(input())

for i in range(1, (n * 2)):
    line = " " * abs(n - i) + "*" * (((n * 2) - 1) - abs((n*2 - i) - i))
    
    print(line)