while True:
    sides = list(map(int, input().split(' ')))
    
    if sum(sides) == 0:
        break
    
    max_side = max(sides)
    max_index = sides.index(max_side)
    
    set_sides = set(sides)
    
    len_sides = len(set_sides)
    
    sides.pop(max_index)
        
    if sum(sides) <= max_side:
        print('Invalid')
    elif len_sides == 1:
        print('Equilateral')
    elif len_sides == 2:
        print('Isosceles')
    else:
        print('Scalene')