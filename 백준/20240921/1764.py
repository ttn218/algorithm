N, M = map(int, input().split(' '))

name_dict = {}

for _ in range(N):
    name = input()
    
    name_dict[name] = 1

듣보잡 = []
for _ in range(M):
    name = input()
    
    if name in name_dict:
        듣보잡.append(name)

듣보잡 = sorted(듣보잡)

print(len(듣보잡))
print('\n'.join(듣보잡))