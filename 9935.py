import sys
input = sys.stdin.readline

origin = input().strip()
bomb = input().strip()
result = []

for i in range(len(origin)):
  result += origin[i]
  if len(result) >= len(bomb):
    if ''.join(result[-len(bomb):]) == bomb:
      for _ in range(len(bomb)):
        result.pop()

if len(result):
  print(''.join(result))
else:
  print('FRULA')