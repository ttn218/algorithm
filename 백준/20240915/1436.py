N = int(input())

count = 1

i = 666

while count < N:
    i += 1
    
    if str(i).find('666') > -1:
        count += 1
        
print(i)