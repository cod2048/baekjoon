import sys
n, m = map(int, input().split())
listen = []
see = []
ls = set()

for i in range(n):
    listen.append(input())

for i in range(m):
    see.append(input())

listen = set(listen)
see = set(see)

ls = listen & see

lst = sorted(list(ls))

print(len(list(lst)))
for i in range(len(lst)):
    print(lst[i])