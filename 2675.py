import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  R, S = input().split()
  for i in list(S):
    print(int(R)*i, end='')
  print('')