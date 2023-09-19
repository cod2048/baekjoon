import sys
input = sys.stdin.readline

def is_prime(n):
  if n < 2:
    return False
  else:
    for i in range(2, n):
      if n % i == 0:
        return False
    return True

N = int(input())
num_list = list(map(int, input().split()))
result = 0

for i in num_list:
  if is_prime(i) == True:
    result += 1

print(result)

