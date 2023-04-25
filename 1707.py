import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def DFS(start):
    visited[start] = True
    for i in a[start]:
        if not visited[i]:
            check[i] = (check[start] + 1) % 2
            DFS(i)
        elif check[start] == check[i]:
            global isEven
            isEven = False

n = int(input())
for i in range(n):
    v, e = map(int, input().split())
    a = [[] for _ in range(v)]
    visited = [False for _ in range(v)]
    check = [0 for _ in range(v)]
    isEven = True
    for j in range(e):
        start, end = map(int, input().split())
        a[start-1].append(end-1)
        a[end-1].append(start-1)
    for j in range(v):
        if not visited[j] and isEven:
            DFS(j)
    if isEven:
        print('YES')
    else:
        print('NO')
