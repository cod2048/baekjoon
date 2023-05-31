import sys
input = sys.stdin.readline

n = int(input())
rope = []
result = []

for _ in range(n):
    x = int(input())
    rope.append(x)

rope.sort(reverse=True)

for i in range(n):
    result.append(rope[i]*(i+1))

print(max(result))

