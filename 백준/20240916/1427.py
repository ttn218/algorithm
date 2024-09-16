def bubbleSort(iterable, desc = False):
    c_iter = [x for x in iterable]
    
    dir_fc = lambda x, y: x < y if desc else x > y
    
    for _ in range(len(c_iter)):
        for j in range(len(c_iter)-1):
            if dir_fc(c_iter[j], c_iter[j + 1]):
                temp = c_iter[j]
                c_iter[j] = c_iter[j + 1]
                c_iter[j + 1] = temp
    return c_iter

n = list(map(int, list(input())))

for x in bubbleSort(n, True):
    print(x, end="")


