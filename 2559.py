import sys
input = sys.stdin.readline

n, k = map(int, input().split())

temp = list(map(int, input().split()))

start = 0
end = k-1
x = 0
    
for i in range(k):
    x += temp[i]
max = x
    
while end < n:
    x -= temp[start]
    start += 1
    end += 1
    if end == n:
        break
    x += temp[end]
    if x > max:
        max = x

print(max)
