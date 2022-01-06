# 영역 구하기
import sys

sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
field = [[0]*m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x2-x1):
        for j in range(y2-y1):
            if field[x1+i][y1+j] != 1:
                field[x1+i][y1+j] = 1

result = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
global sep_count
sep_count = 0


def dfs(x, y):
    global sep_count
    if field[x][y] == 0:
        field[x][y] = 1
        sep_count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if field[nx][ny] == 0:
                dfs(nx, ny)


for i in range(n):
    for j in range(m):
        sep_count = 0
        if field[i][j] == 0:
            dfs(i, j)
            result.append(sep_count)

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')
