import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

min = nums[0]
max = nums[0]

for i in nums[1:]:
    if min > i:
        min = i
    elif max < i:
        max = i

print(min, max)