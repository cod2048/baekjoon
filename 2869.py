import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().split())

# total_distance = 0
# day = 0

# while True:
#   day += 1
#   total_distance += A
#   if total_distance >= V:
#     print(day)
#     break
#   total_distance -= B

print(math.ceil((V-B)/(A-B)))