import sys

input = sys.stdin.readline

n, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

def square(lst1,lst2):
    result = [[0]*n for i in range(n)]
    for i in range(len(lst1)):
        for j in range(len(lst1)):
            for k in range(len(lst1)):
                result[i][j] += lst1[i][k] * lst2[k][j]
                result[i][j] %= 1000 
    return result

def answer(lst, num):
    if num == 1:
        return lst
    elif num % 2 == 0:
        tmp = answer(lst, num//2)
        return square(tmp, tmp)
    else:
        tmp = answer(lst, num//2)
        return square(square(tmp, tmp),lst)
        


result = answer(matrix, b)
for i in range(n):
    for j in range(n):
        print(result[i][j]%1000 , end=" ")
    print()