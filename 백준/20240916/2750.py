result = [int(input()) for _ in range(int(input()))]

def bubbleSort(iterable):
    c_iter = [x for x in iterable]
    
    for _ in range(len(c_iter)):
        for j in range(len(c_iter)-1):
            if c_iter[j] > c_iter[j + 1]:
                temp = c_iter[j]
                c_iter[j] = c_iter[j + 1]
                c_iter[j + 1] = temp
    return c_iter

for n in bubbleSort(result):
    print(n)