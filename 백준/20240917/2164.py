import collections

N = int(input())
cards = collections.deque(range(1, N+1))

while len(cards) > 1:
    cards.popleft()
    if len(cards) == 1:
        break
    cards.rotate(-1)

print(cards[0])