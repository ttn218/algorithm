n = int(input())

s = list(map(lambda x: int(x), input().split(' ')))

m = max(s)

result = sum([x/m*100 for x in s]) / n

print(result)