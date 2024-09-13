x, y, w, h = map(int, input().split(' '))

x1 = abs(w - x)
y1 = abs(h - y)

x2 = abs(0 - x)
y2 = abs(0 - y)

min_v = 1001

for i in [x1 ,y1,x2,y2]:
    if min_v > i:
        min_v = i

print(min_v)