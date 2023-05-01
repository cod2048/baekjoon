import sys
input = sys.stdin.readline

n, m = map(int,input().split())
A = list(map(int, input().split()))
S = [0]
C = [0] * m
answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    x = S[i] % m
    if x == 0:
        answer += 1
    C[x] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)