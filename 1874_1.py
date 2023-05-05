import sys
input = sys.stdin.readline

n = int(input())
lst = [0]*n

for i in range(n):
    lst[i] = int(input())

stack = []
num = 1
answer = ''
result = True

for i in range(n):
    if lst[i] >= num:
        while lst[i] >= num:
            stack.append(num)
            num += 1
            answer += '+\n'
        stack.pop()
        answer += '-\n'
    else:
        x = stack.pop()
        if x > lst[i]:
            print('NO')
            result = False
            break
        else:
            answer += '-\n'

if result: print(answer)