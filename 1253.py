import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0
good = 0

for i in range(n):
    find = nums[i]
    start = 0
    end = n-1
    while start != end:
        good = nums[start] + nums[end]
        if good > find:
            end -= 1
        elif good < find:
            start += 1
        else:
            if start != i and end != i:
                cnt += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1

print(cnt)