import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * n
a = list(map(int, input().split()))
myStack = []

for i in range(n):
    while myStack and a[myStack[-1]] < a[i]:
        ans[myStack.pop()] = a[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1
    
result = ""
for i in range(n):
    sys.stdout.write(str(ans[i]) + " ")
    
print(result)
