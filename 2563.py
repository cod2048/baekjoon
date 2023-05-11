import sys
input = sys.stdin.readline
background = []
for i in range(100):
    row = []
    for j in range(100):
        row.append(0)
    background.append(row)

n = int(input())

for i in range(n):
    x, y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            background[i][j] = 1

cnt = 0

for i in range(100):
    for j in range(100):
       if background[i][j] == 1:
            cnt +=1

print(cnt)
