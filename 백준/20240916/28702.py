def fizzBuzzNumber(n):
    if n == 'Fizz' or n == 'Buzz' or n == 'FizzBuzz':
        return -1, n
    
    return 0, n
    

f1, n1 = fizzBuzzNumber(input())
f2, n2 = fizzBuzzNumber(input())
f3, n3 = fizzBuzzNumber(input())

target = 0


if f1 == 0:
    target = int(n1) + 3
if f2 == 0:
    target = int(n2) + 2
if f3 == 0:
    target = int(n3) + 1

if target % 3 == 0 and target % 5 == 0:
    print('FizzBuzz')
elif target % 3 == 0 and target % 5 != 0:
    print('Fizz')
elif target % 3 != 0 and target % 5 == 0:
    print('Buzz')
else:
    print(target)