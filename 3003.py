original = [1,1,2,2,2,8]
n = list(map(int, input().split()))
result = []

for i in range(6):
    x = original[i] - n[i]
    result.append(x)

for i in range(6):
    print(result[i], end=' ')