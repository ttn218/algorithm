N = int(input())

x_list = list(map(int, input().split(' ')))

sort_list = sorted(x_list)

sorted_dict = {}    
count = 0
for x in sort_list:
    if x not in sorted_dict:
        sorted_dict[x] = count
        count += 1

for x in x_list:
    print(sorted_dict[x], end=" ")
