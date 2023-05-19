import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ans = set()
cnt = 0
    
    
for _ in range(n):
    x = input().strip()
    ans.add(x)

for _ in range(m):
    y = input().strip()
    if y in ans:
        cnt += 1

print(cnt)