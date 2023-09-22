import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
cards = deque()

for i in range(1, N + 1):
  cards.append(i)

while len(cards) >= 2:
  cards.popleft()
  cards.append(cards.popleft())

print(cards[0])