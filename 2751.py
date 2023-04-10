import sys

n = int(input())
list = []
    
for i in range(n):
    x = int(sys.stdin.readline())
    list.append(x)

list.sort()

for i in list:
    print(i)