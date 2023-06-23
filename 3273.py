import sys
input = sys.stdin.readline

def two_pointer(lst, num):
    start = 0
    end = len(lst)-1
    cnt = 0
    while start < end:
        sum_num = nums[start] + nums[end]
        if sum_num == num:
            cnt += 1
            start += 1
            end -= 1
        elif sum_num > num:
            end -= 1
        else:
            start += 1
    return cnt
        

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()

print(two_pointer(nums, x))

