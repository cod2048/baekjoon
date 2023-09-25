import sys
input = sys.stdin.readline

def quick_sort(num_lst, left, right):
  pl = left
  pr = right
  pc = (pl + pr) // 2
  while num_lst[pc]>num_lst[pl]:
    pl += 1
  while num_lst[pc]<num_lst[pr]:
    pr -= 1
  if pl <= pr:
    num_lst[pl], num_lst[pr] = num_lst[pr], num_lst[pl]
    pl += 1
    pr -= 1
  if left < pr:
    quick_sort(num_lst, left, pr)
  if pl < right:
    quick_sort(num_lst, pl, right)
  return num_lst

N = int(input())
nums = []
for _ in range(N):
  nums.append(int(input()))

for i in quick_sort(nums, 0, N-1):
  print(i)