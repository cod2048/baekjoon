import sys
input = sys.stdin.readline

N = int(input())
sticks = []
for _ in range(N):
  sticks.append(int(input()))

r_stick = sticks[-1]
result = 0
see_stick = len(sticks) - 2

while see_stick >= 0:
  if r_stick >= sticks[see_stick]:
    see_stick -= 1
  else:
    r_stick = sticks[see_stick]
    result += 1

print(result + 1)