w = input()

if w == ' ':
    print(0)
else:
    s = w.split(' ')

    if w[0] == ' ':
        s.pop(0)

    if w[-1] == ' ':
        s.pop(-1)

    print(len(s))