import sys
input = sys.stdin.readline

n = int(input())

rainbow = {}
rainbow['ChongChong'] = 1

for _ in range(n):
    a, b = map(str, input().rstrip().split())

    if a not in rainbow:
        rainbow[a] = 0
    if b not in rainbow:
        rainbow[b] = 0

    if rainbow[a] == 1 or rainbow[b] == 1:
        rainbow[a] = 1
        rainbow[b] = 1
    else:
        rainbow[a] = 0
        rainbow[b] = 0

cnt = 0

for value in rainbow.values():
    if value == 1:
        cnt += 1

print(cnt)
