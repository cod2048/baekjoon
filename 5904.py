import sys
input = sys.stdin.readline

n = int(input().strip())

def recursive(total_length, mid_length, n):
    if n <= 3:
        return "moo"[n-1]


    left_length = (total_length - mid_length) // 2

    if n <= left_length:
        return recursive(left_length, mid_length - 1, n)


    if n > left_length + mid_length:
        return recursive(left_length, mid_length - 1, n - left_length - mid_length)

    if n - left_length == 1:
        return "m"
    else:
        return "o"


total_length = 3 
m = 0
while total_length < n:
    m += 1
    total_length = 2 * total_length + m + 3

print(recursive(total_length, m+3, n))