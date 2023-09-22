import sys
input = sys.stdin.readline

N = int(input())

def factorial(num):
  if num == 0:
    return 1
  else:
    return num * factorial(num-1)
  
print(factorial(N))