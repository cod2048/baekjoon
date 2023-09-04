import sys
input = sys.stdin.readline

def euclidean_gcd(a, b):
  while b:
    a, b = b, a % b
  return a

t = int(input())
for _ in range(t):
  a, b = map(int, input().split())
  print(int(a * b / euclidean_gcd(a, b)))