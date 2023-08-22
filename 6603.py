import sys
from collections import deque
input = sys.stdin.readline

result = []

def recursive(lst, n):
  if len(result) == 6:
    print(*result)
    return
  for i in range(len(lst)):
    if lst[i] not in result:
      result.append(lst[i])
      recursive(lst[i+1:], n)
      result.pop()
  
while True:
  test_case = deque(map(int,input().split()))
  m = test_case.popleft()
  if m == 0:
    break
  else:
    recursive(list(test_case), m)
    print()