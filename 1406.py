import sys
from collections import deque

sentence = list(input().strip())
m = int(input())
cursor = deque()

for _ in range(m):
  order = list(input().split())
  if order[0] == 'L' and len(sentence):
    cursor.appendleft(sentence.pop())
  elif order[0] == 'D' and len(cursor):
    sentence.append(cursor.popleft())
  elif order[0] == 'B' and len(sentence):
    sentence.pop()
  elif order[0] == 'P':
    sentence.append(order[1])

for i in sentence:
  print(i, end='')
for i in cursor:
  print(i, end='')
