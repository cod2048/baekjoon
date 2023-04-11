n = int(input())
lst = [0]*n
ans = 0

def queen(a):
    global ans
    if a == n:
        ans += 1
        return
    else:
        for i in range(n):
            lst[a] = i
            if check(a):
                queen(a+1)            


def check(a):
    for i in range(a):
        if lst[a] == lst[i] or abs(lst[a]-lst[i]) == abs(a-i):
            return False
    return True

queen(0)
print(ans)