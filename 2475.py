import sys
input = sys.stdin.readline

num = list(map(int, input().split()))

for i in range(len(num)):
  num[i] = num[i]*num[i]

print(sum(num)%10)