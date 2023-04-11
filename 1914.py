def hanoi(n, x, y):
    if n == 1:
        print(x, y, sep = " ")
        return
    hanoi(n-1, x, 6-x-y)
    print(x, y)
    hanoi(n-1, 6-x-y, y)
    
n = int(input())
if n <= 20:
    print(2 ** n - 1)
    hanoi(n, 1, 3)
else:
    print(2 ** n -1)