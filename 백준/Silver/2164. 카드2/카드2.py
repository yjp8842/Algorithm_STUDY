from collections import deque

N = int(input())
cards = deque(range(N, 0, -1))

while True:
    if len(cards) == 1:
        print(cards[0])
        break
    
    cards.pop()
    cards.appendleft(cards.pop())