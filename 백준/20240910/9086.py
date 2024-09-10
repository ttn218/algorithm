t = int(input())

result = []

for _ in range(t):
    w = input()
    
    result.append(f'{w[0]}{w[-1]}')
    
print('\n'.join(result))