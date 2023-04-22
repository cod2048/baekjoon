n, m = map(int, input().split())
result = [1 * i+1 for i in range(n)]

for k in range(m):
    i, j = map(int, input().split())
    result[i-1], result[j-1] = result[j-1], result[i-1]

for i in range(n):
    print(result[i], end=' ')
