import math

N = int(input())

size_count_list = list(map(int, input().split(' ')))

T, P = map(int, input().split(' '))

t_total = sum([math.ceil(x / T) for x in size_count_list])
p_total = N // P
p_mod = N % P

print(t_total)
print(f'{p_total} {p_mod}')
