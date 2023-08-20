import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
min_num = 0
cards.sort()
sum_num = 0

for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      sum_num = cards[i] + cards[j] + cards[k]
      if sum_num > m:
        break
      elif min_num <= sum_num:
        min_num = sum_num

print(min_num)