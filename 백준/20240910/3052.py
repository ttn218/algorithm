s = []

for _ in range(10):
    x = int(input()) % 42
    
    if x not in s:
        s.append(x)
        
print(len(s))