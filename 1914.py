import sys
input = sys.stdin.readline

def hanoi(num, start, fin):
  if num == 1:
    print(start, fin)
    return
  hanoi(num-1, start, 6-start-fin)
  print(start, fin)
  hanoi(num-1, 6-start-fin, fin)

N = int(input())

print(2**N - 1)
if N <= 20:
  hanoi(N, 1, 3)