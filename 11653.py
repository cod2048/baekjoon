import sys
input = sys.stdin.readline

N = int(input())
result = []

while True:
  if N == 1:
    break
  for i in range(2, N+1):
    if N % i == 0:
      result.append(i)
      N = N//i
      break

for i in range(len(result)):
  print(result[i])
