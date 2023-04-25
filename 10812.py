n, m = map(int, input().split())

result = [i+1 for i in range(n)]

for l in range(m):
    i,j,k = map(int, input().split())
    result = result[:i-1] + result[k-1:j] + result[i-1:k-1] + result[j:]

print(*result)