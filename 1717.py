import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sets = []

for i in range(n+1):
    s = set()
    s.add(i)
    sets.append(s)

for i in range(m):
    x, a, b = map(int, input().strip().split())
    j = 0
    if x == 0:
        while True:
            

print(sets)
    # else:
    #     if b in sets[a] or a in sets[b]:
    #         print('YES')
    #     else:
    #         print('NO')