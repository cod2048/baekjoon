import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

length = 100001
start = 0
end = 0
sum_num = nums[0]

while start <= end:
    if sum_num >= s:
        length = min(length, end-start + 1)
        sum_num -= nums[start]
        start += 1
    else:
        end += 1
        if end < n :
            sum_num += nums[end]
        else:
            break

if length == 100001:
    print(0)
else:
    print(length)
