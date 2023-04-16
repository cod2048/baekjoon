import sys
input = sys.stdin.readline

n = int(input())
stick = []
count = 0

for i in range(n):
    s = int(input())
    stick.append(s)

for i in range(1, n):
    if stick[-1] < stick[-1-i]:
        count += 1
        stick[-1] = stick[-1-i]

print(count+1)
