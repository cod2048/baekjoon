import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lan_line = []

def binary_search(lst, target):
  start = 1
  end = max(lst)
  result = 0
  while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(len(lst)):
      cnt += lst[i] // mid
    if cnt < target:
      end = mid - 1
    else:
      start = mid + 1
      result = max(result, mid)

  print(result)

for _ in range(n):
  tmp = int(input().strip())
  lan_line.append(tmp)

binary_search(lan_line, k)
