n = input()

n1, n2, n3 = map(lambda d: int(d),n.split(' '))

result = 0

if n1 == n2 == n3:
    result = 10000 + n1 * 1000

elif n1 == n2 or n1 == n3:
    result = 1000 + n1 * 100

elif n2 == n3:
    result = 1000 + n2 * 100

else:
    result = max([n1,n2,n3]) * 100

print(result)