import sys
input = sys.stdin.readline

def euclidean_gcd(x, y):
  while y:
    x, y = y, x % y
  return x

a, b = map(int, input().split())
gcd = euclidean_gcd(a, b)
print('1' * gcd)
