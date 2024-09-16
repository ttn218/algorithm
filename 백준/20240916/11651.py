def merge(list_1:list, list_2:list):
    sorted_list = []
    index_1 = 0
    index_2 = 0

    while index_1 < len(list_1) and index_2 < len(list_2):
        if list_1[index_1][1] < list_2[index_2][1] or (list_1[index_1][1] == list_2[index_2][1] and list_1[index_1][0] < list_2[index_2][0]):
            sorted_list.append(list_1[index_1])
            index_1 += 1
        else:
            sorted_list.append(list_2[index_2])
            index_2 += 1
            
    if index_1 < len(list_1):
        sorted_list += list_1[index_1:]
    else:
        sorted_list += list_2[index_2:]
    
    
    return sorted_list

def mergeSort(iterable):
    len_iter = len(iterable)
    
    if len_iter >= 2:
        return merge(mergeSort(iterable[0: len_iter//2]), mergeSort(iterable[len_iter//2:]))
    
    return iterable


N = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(N)]

arr = mergeSort(arr)

for x, y in arr:
    print(f'{x} {y}')