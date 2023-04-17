import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
result = deque([])

for i in range(n):
    x = input().split()
    if x[0] == 'push':
        result.append(x[1])
    elif x[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.popleft())
    elif x[0] == 'size':
        print(len(result))
    elif x[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 'front':
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])
    elif x[0] == 'back':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])