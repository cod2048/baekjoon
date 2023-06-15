import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 1

visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if not visited[nx][ny] and graph[nx][ny] > h:
                    queue.append((nx, ny))
                    visited[nx][ny] = True         

for k in range(1, 101):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > k:
                bfs(i, j, k)
                cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
    if cnt == 0:
        break


print(max_cnt)