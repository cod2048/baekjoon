n, m = map(int, input().split())

result = [1*i+1 for i in range(n)]

for k in range(m):
    i, j = map(int, input().split())
    result[i-1 :j] = reversed(result[i-1:j])

for i in range(n):
    print(result[i], end = ' ')