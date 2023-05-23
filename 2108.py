import sys
input = sys.stdin.readline

n = int(input())
nums = []
dic = {}

for _ in range(n):
    num = int(input().strip())
    nums.append(num)
    if num in dic:
        dic[num] = dic[num] +1
        continue
    dic[num] = 1


nums.sort()
dic = list(sorted(dic.items(), key = lambda x: (-x[1], x[0])))

print(round(sum(nums)/len(nums)))

center = len(nums)//2
print(nums[center])

if len(dic) != 1:
    if dic[0][1] == dic[1][1]:
        print(dic[1][0])
    else:
        print(dic[0][0])
else:
    print(dic[0][0])


print(max(nums)-min(nums))