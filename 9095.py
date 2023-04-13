n = int(input())

def n_sum(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else :
        return n_sum(n-1) + n_sum(n-2) + n_sum(n-3)

for i in range(n):
    n = int(input())
    print(n_sum(n))
