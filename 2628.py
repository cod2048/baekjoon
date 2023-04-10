x, y = map(int, input().split())
cut = int(input())
x_cut = [0]
y_cut = [0]

for i in range(cut):
    a, b = map(int, input().split())
    if a == 0:
        x_cut.append(b)
    else:
        y_cut.append(b)

x_cut.append(y)
y_cut.append(x)

x_cut = sorted(x_cut)
y_cut = sorted(y_cut)

x_max = 0
for i in range(1, len(x_cut)):
    if (x_cut[i] - x_cut[i-1]) > x_max:
        x_max = x_cut[i] - x_cut[i-1]

y_max = 0
for i in range(1, len(y_cut)):
    if (y_cut[i] - y_cut[i-1]) > y_max:
        y_max = y_cut[i] - y_cut[i-1]

print(x_max * y_max)
