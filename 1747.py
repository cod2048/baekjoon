import sys
input = sys.stdin.readline

m = 1000001

prime = [True] * m
prime[0] = prime[1] = False

p = 2

while True:
    if p >= m:
        break
    if prime[p]:
        for j in range(p+p, m, p):
            prime[j] = False
    p += 1

n = int(input())

for k in range(n, m):
    if prime[k] and str(k) == str(k)[::-1]:
        print(k)
        break