def bubbleSort(iterable):
    c_iter = [x for x in iterable]
    
    for _ in range(len(c_iter)):
        for j in range(len(c_iter)-1):
            if c_iter[j] > c_iter[j + 1]:
                temp = c_iter[j]
                c_iter[j] = c_iter[j + 1]
                c_iter[j + 1] = temp
    return c_iter

result = bubbleSort([int(input()) for _ in range(5)])

avg = sum(result) / len(result)
mid = result[2]

print(int(avg))
print(mid)