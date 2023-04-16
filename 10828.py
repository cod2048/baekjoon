import sys
input = sys.stdin.readline
stack = []

n= int(input())

for i in range(n):
    x = input().split()
    if x[0] == 'push':
        stack.append(x[1])
    elif x[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif x[0] == 'size':
        print(len(stack))
    elif x[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()