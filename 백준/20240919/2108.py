import sys
N = int(input())

number_dict = {}
numbers = []

max_count = 0

for _ in range(N):
    n = int(sys.stdin.readline())
    
    if n in number_dict:
        number_dict[n] += 1
    else:
        number_dict[n] = 1
    
    if max_count < number_dict[n]:
        max_count = number_dict[n]
    
    numbers.append(n)

targets = []

for i, v in number_dict.items():
    if max_count == v:
        targets.append(i)

sorted_numbers = sorted(numbers)
sorted_targets = sorted(targets)

print(round(sum(sorted_numbers) / N))
print(sorted_numbers[int(N/2)])
print(sorted_targets[0] if len(sorted_targets) == 1 else sorted_targets[1])
print(sorted_numbers[-1] - sorted_numbers[0])

