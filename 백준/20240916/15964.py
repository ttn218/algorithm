def fun(a, b):
    return (a+b)*(a-b)

A, B = map(int, input().split(' '))

print(fun(A, B))