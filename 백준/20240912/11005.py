N, B = input().split(' ')

def basetransfor(n, b):
    result = ''
    
    while n > 0:
        n, mod = divmod(n, b)
        
        if mod >= 10:
            result += chr(mod+55)
        else:
            result += str(mod)
    
    return result[::-1]

print(basetransfor(int(N), int(B)))