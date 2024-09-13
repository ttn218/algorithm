str_arr = []

max_lenth = -1

for _ in range(5):
    s = input()
    s_lenth = len(s)
    max_lenth = s_lenth if max_lenth < s_lenth else max_lenth
    str_arr.append(s)

result = ''

for j in range(max_lenth):
    for i in range(5):
        if len(str_arr[i]) > j:
            result += str_arr[i][j]

print(result)