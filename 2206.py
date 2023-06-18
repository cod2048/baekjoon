import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, (input().split()))
graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    flag = False
    visited[x][y] = True

    while queue :
        cx, cy = queue.popleft()
        for i in range(4) :
            nx, ny = cx + dx[i], cy + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if flag == False and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    flag = True
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

bfs(0, 0)
for i in range(n):
    for j in range(m):
        if visited[i][j] == True:
            count += 1
print(count)