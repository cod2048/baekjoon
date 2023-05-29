import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
position = list(map(int, input().split()))
result = deque()
cnt = 0

for i in range(1, n+1):
    result.append(i)

for i in range(len(position)):
    while True:
        if result[0] == position[i]:
            result.popleft()
            break
        else:
            while result[0] != position[i]:
                if result.index(position[i]) < len(result)/2:
                    result.append(result.popleft())
                    cnt += 1
                else:
                    result.appendleft(result.pop())
                    cnt += 1

print(cnt)
