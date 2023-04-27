import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input().strip()))

result = 0

for i in range(n):
    cnt = 0
    vertical = 1
    for j in range(m):
        if graph[i][j] == '|':
            vertical = 1
        else:
            if vertical == 1:
                cnt += 1
            vertical = 0

    result += cnt

for i in range(m):
    cnt = 0
    vertical = 0
    for j in range(n):
        if graph[j][i] != '|':
            vertical = 0
        else:
            if vertical == 0:
                vertical = 1
                cnt += 1
    result += cnt

print(result)