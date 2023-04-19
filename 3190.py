import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [[0] * n for i in range(n)]

k = int(input())
for i in range(k):
    apple = list(map(int, input().split()))
    board[apple[0]-1][apple[1]-1] = 2
l = int(input())
turntimes = deque([list(map(str,input().split())) for i in range(l)])

queue = deque([[0,0]])
directions = [[0,1],[1,0],[0,-1],[-1,0]]
x, y , direction, time = 0, 0, 0, 0
while True:
    time += 1
    x += directions[direction][0]
    y += directions[direction][1]

    if x < 0 or x > n-1 or y < 0 or y > n-1:
        break
    if board[x][y] == 2:
        board[x][y] = 1
        queue.append([x,y])
    elif board[x][y] == 0:
        board[x][y] = 1
        queue.append([x, y])
        tail = queue.popleft()
        board[tail[0]][tail[1]] = 0
    else:
        break

    if turntimes:
        if str(time) == turntimes[0][0]:
            if turntimes[0][1] == 'L':
                direction = (direction -1)%4
                turntimes.popleft()
            else:
                direction = (direction +1)%4
                turntimes.popleft()

print(time)