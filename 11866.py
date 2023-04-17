from collections import deque

n, k = map(int, input().split())

ysps = []
queue = deque()

for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())

    ysps.append(queue.popleft())

print('<', end="")
for i in range(len(ysps)-1):
    print(ysps[i], end= ', ')
print(ysps[-1], end=">")