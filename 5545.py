

import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())
d = []

for _ in range(n):
    cal = int(input())
    d.append(cal)

d.sort(reverse = True)
cal = c
result = c / a

for cals in d:
    new_cal = cal + cals
    new_price = a + b   

    if new_cal / new_price > result:
        result = new_cal / new_price

        cal = new_cal
        a = new_price
    else:
        break

print(int(result))

