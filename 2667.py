n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, list(input().strip()))))

result = []

def dfs(r, c):
    global count
    count += 1
    visited[r][c] = True
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and graph[nr][nc] == 1:
            dfs(nr, nc)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])
