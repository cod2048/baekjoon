import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    queue = deque()
    cnt = 0
    for i in range(len(lst)):
        queue.append((i,lst[i]))
    while queue:
        idx, ipt = queue.popleft()
        flag = True
        for i in range(len(queue)):
            if ipt < queue[i][1]:
                flag = False
                break
        if flag:
            cnt += 1
            if idx == m:
                break
        else:
            queue.append((idx, ipt))
    print(cnt)