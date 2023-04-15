import sys
input = sys.stdin.readline
num = []
result = []

for i in range(10):
    num.append(int(input()))

for i in range(10):
    if (num[i]%42) in result:
        continue
    else:
        result.append(num[i]%42)

print(len(result))