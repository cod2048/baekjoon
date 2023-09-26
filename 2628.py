import sys
input = sys.stdin.readline

x, y = map(int, input().split())
cut_x = [0, y]
cut_y = [0, x]

cut = int(input())
for i in range(cut):
    x_y, where = map(int, input().split())
    if x_y == 0:
        cut_x.append(where)
    else:
        cut_y.append(where)
cut_x.sort()
cut_y.sort()

max_x = 0
max_y = 0
for i in range(1, len(cut_x)):
    if cut_x[i] - cut_x[i-1] > max_x:
        max_x = cut_x[i] - cut_x[i-1]

for i in range(1, len(cut_y)):
    if cut_y[i] - cut_y[i-1] > max_y:
        max_y = cut_y[i] - cut_y[i-1]

print(max_x*max_y)