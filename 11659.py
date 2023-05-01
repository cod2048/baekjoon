import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

s_nums = [0]
x = 0

for i in range(n):
    x += nums[i]
    s_nums.append(x)

for _ in range(m):
    i, j = map(int, input().split())
    print(s_nums[j] - s_nums[i-1])