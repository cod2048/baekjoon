import sys
input = sys.stdin.readline

sound = list(map(int,input().split()))

asc_sound = sorted(sound)
des_sound = sorted(sound, reverse=True)

if sound == asc_sound:
  print('ascending')
elif sound == des_sound:
  print('descending')
else:
  print('mixed')
