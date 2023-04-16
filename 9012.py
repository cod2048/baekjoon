import sys
input = sys.stdin.readline

t = int(input())
    
for i in range(t):
    ps = []
    x = input()
    for k in x:
        if k == '(':
            ps.append(k)
        elif k == ')':
            if len(ps) == 0:
                print('NO')
                break
            ps.pop()
    else:
        if len(ps) == 0:
            print('YES')
        else:
            print('NO')
