w = input().upper()

dic = {}

for c in w:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
        
maxv = max(dic.values())    
maxk = ""
c = 0
for key, v in dic.items():
    if (v == maxv):
        c +=1
        maxk = key

if c > 1:
    print("?")
else:
    print(maxk)