N = int(input())
cards1 = list(map(int, input().split(' ')))

M = int(input())
cards2 = list(map(int, input().split(' ')))
counts = [0] * 20000002

for card in cards1:
    counts[card + 10000001] += 1
    
for card in cards2:
    print(counts[card + 10000001], end=" ")