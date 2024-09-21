
store = {

}

def fibonacci(n, stock = [0, 0]):
    global store
    
    if n in store:
        
        newStock = [store[n]['stock'][0], store[n]['stock'][1]]
        return store[n]['value'], newStock
    
    if n == 0:
        newStock = [stock[0] + 1, stock[1]]
        return 0, newStock
    elif n == 1:
        newStock = [stock[0], stock[1] + 1]
        return 1, newStock
    else:
        n1, stock1 = fibonacci(n-1, stock)
        n2, stock2 = fibonacci(n-2, stock)
        
        newStock = [stock1[0] + stock2[0], stock1[1] + stock2[1]]
        
        store[n] = {
            "value": n1+n2,
            "stock": newStock
        }
        
        return (n1 + n2), newStock

T = int(input())

for _ in range(T):
    _, stock = fibonacci(int(input()))
    
    print(f'{stock[0]} {stock[1]}')

