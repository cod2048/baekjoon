import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
nums.sort()

start = 0
end = n-1
cnt = 0

while start < end:
    if nums[start] + nums[end] > m:
        end -= 1
    elif nums[start] + nums[end] < m:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1

print(cnt)