w = input()

s = ['-1' for _ in range(26)]

for i, c in enumerate(w):
    if s[ord(c) - 97] == '-1':
        s[ord(c) - 97] = str(i)
    
print(' '.join(s))