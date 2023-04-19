import sys
import heapq

input = sys.stdin.readline

n = int(input())

left = []
right = []
nums = []

for i in range(n):
    x = int(input())
    if len(left) == len(right):
        heapq.heappush(left, (-x, x))
    else:
        heapq.heappush(right, (x, x))
    
    if right and left[0][1] > right[0][0]:
        min = heapq.heappop(right)[0]
        max = heapq.heappop(left)[1]
        heapq.heappush(left, (-min,min))
        heapq.heappush(right, (max,max))

    nums.append(left[0][1])

for j in nums:
    print(j)

