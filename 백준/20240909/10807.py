n = int(input())

numbers = input().split(' ')

target = int(input())

count = 0

for i in range(n):
    if target == int(numbers[i]):
        count += 1

print(count)