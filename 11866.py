import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
people = deque([i for i in range(1, N+1)])
result = []

while len(people):
  for _ in range(K-1):
    people.append(people.popleft())
  result.append(people.popleft())

print('<', end='')
for i in range(N-1):
  print(result[i], end=', ')
print(result[-1], end=">")