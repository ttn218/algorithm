while True:
    n = input()
    
    if n == '0':
        break
    
    list_n = list(n)
    list_n.reverse()
    
    if n == ''.join(list_n):
        print('yes')
    else:
        print('no')