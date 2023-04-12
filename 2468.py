import sys

sys.setrecursionlimit(10000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

fld = []
chk = []
N = 0
minh = 1000
maxh = 0


def dfs(x, y, h):
    global fld, chk, N, dx, dy

    chk[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not chk[nx][ny] and fld[nx][ny] > h:
            dfs(nx, ny, h)


def count_safe_zone(h):
    global fld, chk, N, dx, dy

    chk = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if not chk[i][j] and fld[i][j] > h:
                dfs(i, j, h)
                cnt += 1

    return cnt


def main():
    global fld, N, minh, maxh

    N = int(input())

    fld = []
    for _ in range(N):
        row = list(map(int, input().split()))
        fld.append(row)
        minh = min(minh, min(row))
        maxh = max(maxh, max(row))

    ans = 1
    for h in range(minh, maxh + 1):
        cnt = count_safe_zone(h)
        ans = max(ans, cnt)

    print(ans)

main()
