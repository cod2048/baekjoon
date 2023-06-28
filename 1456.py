import sys
input = sys.stdin.readline

a, b = map(int, input().split())

prime = [0] * 10000001

for i in range(10000001):
    prime[i] = i

prime[1] = 0

p = 2

while p < len(prime):
    if prime[p] != 0:
        for j in range(p*p, len(prime), p):
            prime[j] = 0
    p += 1

cnt = 0

for k in range(2, 10000001):
    if prime[k] != 0:
        temp = prime[k]
        while prime[k] <= b / temp:
            if prime[k] >= a / temp:
                cnt += 1
            temp = temp * prime[k]

print(cnt)
