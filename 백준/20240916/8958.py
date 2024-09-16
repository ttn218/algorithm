T = int(input())

for _ in range(T):
    quiz_result = input()
    combo = 0
    
    total = 0
    for q in quiz_result:
        if q == 'O':
            total += 1 + combo
            combo += 1
        else:
            combo = 0
    
    print(total)
    