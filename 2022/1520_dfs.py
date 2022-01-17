# 내리막 길
import sys
sys.setrecursionlimit(10**9)

m, n = map(int, input().split())

dmap = [list(map(int, input().split())) for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
c = [[-1]*n for _ in range(m)]


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if c[x][y] != -1:
        return c[x][y]
    c[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if dmap[x][y] > dmap[nx][ny]:
                c[x][y] += dfs(nx, ny)
    return c[x][y]


print(dfs(0, 0))
