import sys
input = sys.stdin.readline

n, kim, im = map(int, input().split())
cnt = 1

for i in range(n):
    if kim//2 != im //2 and (kim + 1 == im or im + 1 == kim):
        break
    else:
        if kim%2 == 0:
            kim = kim // 2
        else:
            kim = kim // 2 +1
        if im%2 == 0:
            im = im // 2
        else:
            im = im // 2 + 1
    cnt += 1

print(cnt)