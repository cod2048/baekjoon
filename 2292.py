n = int(input())

ans = 1

for i in range(n):
    ans += (i*6)
    if n <= ans:
        print(i+1)
        break