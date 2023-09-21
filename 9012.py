import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  VPS = input().strip()
  result = []
  for i in VPS:
    if i == '(':
      result.append(i)
    else:
      if len(result) == 0:
        print('NO')
        break
      else:
        result.pop()
  else:
    if len(result) != 0:
        print('NO')
    else:
        print('YES')
