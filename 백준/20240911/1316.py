t = int(input())

group_count = 0

for _ in range(t):
    w = input()
    
    dic = {}
    for i, c in enumerate(w):
        if c in dic:
            if dic[c] + 1 < i:
                break
            
            dic[c] = i
            
        else:
            dic[c] = i
            
        if i == len(w) - 1:
            group_count += 1

print(group_count)