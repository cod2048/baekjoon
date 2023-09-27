import sys
input = sys.stdin.readline

N = int(input())
nums = str(input().strip())
result = 0

for i in range(len(nums)):
  result += int(nums[i])

print(result)