import sys
input = sys.stdin.readline

N = int(input())
N_lst = sorted(list(map(int, input().split())))
M = int(input())
M_lst = list(map(int, input().split()))

def binary_search(lst, num):
  pl = 0
  pr = len(lst) - 1
  while pl <= pr:
    pc = (pl+pr) // 2
    if lst[pc] == num:
      return 1
    elif lst[pc] < num:
      pl = pc + 1
    else:
      pr = pc - 1
  return 0
  
for i in range(len(M_lst)):
   print(binary_search(N_lst, M_lst[i]))