import sys

n = int(input())
list = [0]*10001
    
for _ in range(n):
    x = int(sys.stdin.readline())
    list[x] += 1

for i in range(10001):
    if list[i] != 0:
        for j in range(list[i]):
            print(i)