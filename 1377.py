import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append((int(input()), i))

s_lst = sorted(lst)

max = 0
for i in range(n):
    if max < s_lst[i][1]-i:
        max = s_lst[i][1]-i

print(max+1)


