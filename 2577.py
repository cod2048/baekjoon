import sys
input = sys.stdin.readline
A = int(input())
B = int(input())
C = int(input())
multiple_num = str(A*B*C)
result = [0]* 10

for i in range(10):
  for j in range(len(multiple_num)):
    if str(i) == multiple_num[j]:
      result[i] += 1

print(*result, sep='\n')