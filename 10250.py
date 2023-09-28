import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  H, W, N = map(int, input().split())
  room_num = N//H + 1
  stair = N%H
  if stair == 0:
    stair = H
    room_num -= 1
  print(stair, end='')
  if room_num < 10:
    print(0, end='')
    print(room_num)
  else:
    print(room_num)