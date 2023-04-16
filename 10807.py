import sys
input = sys.stdin.readline

count = 0
n = int(input())

nums = list(map(int, input().split()))

num = int(input())

for i in range(len(nums)):
    if nums[i] == num:
        count += 1

print(count)