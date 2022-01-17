# 유기농 배추
import sys
sys.setrecursionlimit(10**6)

t = int(input())
result = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, m, n):
    field[x][y] = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n:
            if field[nx][ny] == 1:
                dfs(nx, ny, m, n)


for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0]*n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1

    count = 0

    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                dfs(i, j, m, n)
                count += 1
    result.append(count)

for i in result:
    print(i)
