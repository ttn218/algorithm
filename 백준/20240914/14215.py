a, b, c = map(int, input().split(' '))

sides = [a,b,c]

max_side = max(sides)
max_index = sides.index(max_side)
sides.pop(max_index)

sum_sides = sum(sides)

if sum_sides > max_side:
    print(sum_sides+max_side)
else:
    print(sum_sides*2 - 1)