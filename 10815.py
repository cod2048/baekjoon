import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
find_cards = list(map(int, input().split()))
result = []
cards.sort()

def binary_search(num, num_list):
  start = 0
  end = len(num_list)-1
  while start<=end:
    mid = (start+end)//2
    if num == num_list[mid]:
      return 1
    elif num < num_list[mid]:
      end = mid-1
    else:
      start = mid+1
  return 0
    

    
  
for i in range(m):
  result.append(binary_search(find_cards[i], cards))

print(*result)