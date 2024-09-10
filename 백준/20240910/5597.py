numbers = [x for x in range(1, 31)]

for _ in range(28):
    x = int(input())
    
    numbers.remove(x)
    
print(numbers[0])
print(numbers[1])