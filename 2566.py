result = []
max_val = 1

for i in range(9):
    x = list(map(int, input().split()))
    if max_val < max(x):
        max_val = max(x)
        result = [max_val, i, x.index(max_val)]

print(result[0])
print(result[1]+1, result[2]+1)
