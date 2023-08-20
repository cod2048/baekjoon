import sys
input = sys.stdin.readline

n = int(input().strip())
result = 0

for i in range(1, n+1):
  num = i
  sum = i
  while num != 0:
    sum += num % 10
    num = num // 10
  if sum == n:
    result = i
    break
print(result)