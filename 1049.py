import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

min_price = 10000000000
p_package = []
p_single = []

for _ in range(m):
    package, single = map(int, input().rstrip().split())
    p_package.append(package)
    p_single.append(single)

min_package = min(p_package)
min_single = min(p_single)

min_total = (min_package * (n//6)) + (min_single * (n % 6))
min_package = min_package * (n//6 + 1)
min_single = min_single * n

result = min(min_total, min_package, min_single)

print(result)
