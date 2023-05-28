import sys
input = sys.stdin.readline

n = int(input())
measure = list(map(int, input().split()))

print(min(measure) * max(measure))

