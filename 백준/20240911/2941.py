dic = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

w = input()


total = 0
for c in dic:
    if c in w:
        d = w.split(c)
        total += len(d) - 1
        
        w = " ".join(d)
    

total += len("".join(w.split(" ")))


print(total)