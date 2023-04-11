def z(n, r, c):
    if n == 0:
        return 0
    print((2*(r%2)+(c%2)))
    return((2*(r%2)+(c%2))+4*(z(n-1, r//2, c//2)))

n, r, c = map(int, input().split())

print(z(n, r, c))






