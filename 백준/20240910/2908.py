n1, n2 = input().split(' ')

n1 = f'{n1[2]}{n1[1]}{n1[0]}'
n2 = f'{n2[2]}{n2[1]}{n2[0]}'

if int(n1) > int(n2):
    print(n1)
else:
    print(n2)