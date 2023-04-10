import sys

n = int(sys.stdin.readline())
old_list = []

for i in range(n):
    old_list.append(sys.stdin.readline().strip())
new_list = set(old_list)
old_list = list(new_list)
old_list.sort()
old_list.sort(key = len)
for i in old_list:
    print(i)