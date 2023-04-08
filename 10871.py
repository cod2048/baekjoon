n, x = input().split()

n = int(n)
x = int(x)

a = list(map(int, input().split()))

for i in range(0, n):
    if x > a[i]:
        print(a[i], end=' ')