import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
mydeque = deque();
number = list(map(int, input().split()))

for i in range(n):
    while mydeque and mydeque[-1][0] > number[i]:
        mydeque.pop()
    mydeque.append((number[i], i))
    if mydeque[0][1] <= i - l:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')