import sys
sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
nums = []


while True:
    try:
        n = int(input())
        nums.append(n)
    except:
        break

def postorder(start,end):
    if start > end:
        return
    s = nums[start]
    e = end+1
    for i in range(start+1, end+1):
        if s < nums[i]:
            e = i
            break
    postorder(start+1,e-1)
    postorder(e,end)

    print(nums[start])

postorder(0,len(nums)-1)
