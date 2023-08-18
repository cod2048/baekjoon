import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
  
for i in range(m):
  a.append(b[i])

print(*sorted(a))