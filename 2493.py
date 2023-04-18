#시간 초과 뜸

# import sys
# input = sys.stdin.readline

# n = int(input())

# top = list(map(int, input().split()))
# result = [0 for _ in range(n)]

# def raser(x, y):
#     if abs(x)>y-1:
#         return
#     for i in range(1, y):
#         if top[-x] < top[-x+i]:
#             result[-x] = -x+i+1
#     raser(x+1, y)

# raser(1, n)

# for i in range(len(result)):
#     print(result[i], end=" ")

N = int(input())
top_list = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > top_list[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, top_list[i]])

print(" ".join(map(str, answer)))