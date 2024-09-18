N, K = map(int, input().split(' '))

humans = list(range(1, N+1))
deletes = []

cursor = 0
while len(humans) > 0:
    cursor = (cursor + K -1) % len(humans)
    
    deletes.append(str(humans.pop(cursor)))
    

print(f'<{", ".join(deletes)}>')