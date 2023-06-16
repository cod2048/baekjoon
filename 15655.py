import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
result = []

def dfs(depth, idx):
    if len(result) == m:
        print(*result)
        return
    for j in range(idx+1, n):
        result.append(nums[j])
        dfs(depth+1, j)
        result.pop()

for i in range(n):
    result.clear()
    result.append(nums[i])
    dfs(1,i)
