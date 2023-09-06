import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
a = [[]for _ in range(n+1)]
result = []
visited = [-1] * (n+1)

def bfs(v):
  queue = deque()
  queue.append(v)
  visited[v] += 1
  while queue:
    node = queue.popleft()
    for i in a[node]:
      if visited[i] == -1:
        visited[i] = visited[node] + 1
        queue.append(i)

for _ in range(m):
  s, e = map(int, input().split())
  a[s].append(e)

bfs(x)

for i in range(n+1):
  if visited[i] == k:
    result.append(i)

if not result:
  print(-1)
else:
  result.sort()
  for i in result:
    print(i)