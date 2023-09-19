import sys
input = sys.stdin.readline

N = int(input())
result = 1
for i in range(N):
  result += result * i

print(result)