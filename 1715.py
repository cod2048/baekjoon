import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
result = 0

for i in range(n):
    heapq.heappush(cards, int(input()))
        
while len(cards) > 1:
    plus = heapq.heappop(cards) + heapq.heappop(cards)
    result += plus
    heapq.heappush(cards, plus)

print(result)