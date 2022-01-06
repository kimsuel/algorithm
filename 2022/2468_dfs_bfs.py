# 안전 영역
import sys

sys.setrecursionlimit(10000)

n = int(input())

field = [list(map(int, input().split())) for _ in range(n)]

max_num = max(map(max, field))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 1


def dfs(x, y, h):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and field[nx][ny] > h:
                visited[nx][ny] = True
                dfs(nx, ny, h)


for k in range(max_num):
    visited = [[False]*n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if field[i][j] > k and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, k)
                count += 1

    answer = max(answer, count)

print(answer)
