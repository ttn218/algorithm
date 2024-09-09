n = input()

numbers = n.split(' ')

s = 0
for number in numbers:
    s+= int(number)

print(s)