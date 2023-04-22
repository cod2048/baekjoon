import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    result[i-1:j] = [k] * (j - i + 1)

for i in range(n):
    print(result[i], end= ' ')