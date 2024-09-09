total = int(input())

t_count = int(input())

s = 0
for i in range(t_count):
    price, count = map(lambda x: int(x), input().split(' '))

    s += price * count

result = "Yes" if total == s else "No"

print(result)