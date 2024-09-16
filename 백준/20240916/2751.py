import sys

def merge(list_1:list, list_2:list, desc=False):
    sorted_list = []
    index_1 = 0
    index_2 = 0

    while index_1 < len(list_1) and index_2 < len(list_2):
        
        if desc:
            if list_1[index_1] >= list_2[index_2]:
                sorted_list.append(list_1[index_1])
                index_1 += 1
            else:
                sorted_list.append(list_2[index_2])
                index_2 += 1
        else:
            if list_1[index_1] <= list_2[index_2]:
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

def mergeSort(iterable, desc=False):
    len_iter = len(iterable)
    
    if len_iter >= 2:
        return merge(mergeSort(iterable[0: len_iter//2], desc), mergeSort(iterable[len_iter//2:], desc), desc)
    
    return iterable
    
    
result = mergeSort([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])


for x in result:
    print(x)