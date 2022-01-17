# 빙산
import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

ice_mountain = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, visited):
    if not visited[x][y]:
        visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if ice_mountain[nx][ny] != 0 and not visited[nx][ny]:
                dfs(nx, ny, visited)


def ice():
    global ice_mountain
    temp_ice = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ice_mountain[i][j] != 0:
                count = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if ice_mountain[nx][ny] == 0:
                            count += 1
                temp_ice[i][j] = ice_mountain[i][j] - count
                if temp_ice[i][j] < 0:
                    temp_ice[i][j] = 0

    ice_mountain = temp_ice


result = 0

while True:
    ice_count = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ice_mountain[i][j] != 0 and not visited[i][j]:
                dfs(i, j, visited)
                ice_count += 1
    if ice_count < 2:
        ice()
        result += 1
    else:
        break

print(result)
