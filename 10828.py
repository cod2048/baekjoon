import sys
input = sys.stdin.readline

N = int(input())
stk = []

for _ in range(N):
  order = list(map(str, input().split()))
  if order[0] == 'push':
    stk.append(order[1])
  elif order[0] == 'top':
    if len(stk) == 0:
      print(-1)
    else:
      print(stk[-1])
  elif order[0] == 'size':
    print(len(stk))
  elif order[0] == 'empty':
    if len(stk) == 0:
      print(1)
    else:
      print(0)
  elif order[0] == 'pop':
    if len(stk) == 0:
      print(-1)
    else:
     print(stk.pop())
  