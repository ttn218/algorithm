numbers = [int(input()) for _ in range(3)]

if numbers[0] == numbers[1] == numbers[2] == 60:
    print('Equilateral')
elif sum(numbers) != 180:
    print('Error')
elif numbers[0] == numbers[1] or numbers[1] == numbers[2] or numbers[0] == numbers[2]:
    print('Isosceles')
else:
    print('Scalene')