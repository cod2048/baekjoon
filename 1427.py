import sys
input = sys.stdin.readline

lst = list(input().strip())

for i in range(len(lst)):
    max = i
    for j in range(i+1, len(lst)):
        if lst[j] > lst[max]:
            max = j
    if lst[max] > lst[i]:
        temp = lst[i]
        lst[i] = lst[max]
        lst[max] = temp

for i in lst:
    print(i, end='')