N = int(input())

arr = []

for _ in range(N):
    word = input()

    if word not in arr:
        arr.append(word)
        
arr = sorted(arr)
arr = sorted(arr, key=len)

for word in arr:
    print(word)