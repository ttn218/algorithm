N = int(input())

arr = []

for _ in range(N):
    age, name = input().split(' ')
    
    arr.append({"age": int(age), "name": name})
    
arr = sorted(arr, key=lambda x: x["age"])

for item in arr:
    print(f'{item["age"]} {item["name"]}')