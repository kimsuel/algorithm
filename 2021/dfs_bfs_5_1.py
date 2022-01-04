# 빙산

import copy

n, m = map(int, input().split())

iceberg = [list(map(int, input().split())) for _ in range(n)]
# iceberg_tmp = copy.deepcopy(iceberg)

queue = []
nx = [0, 1, 0, -1]
ny = [1, 0, -1, 0]
year = 1

def bfs(x, y):
    queue.append([x, y])
    check[x][y] = 1
    while queue:
        fx, fy = queue.pop(0)
        for i in range(4):
            dx = fx + nx[i]
            dy = fy + ny[i]
            if 0 <= dx < n and 0 <= dy < m:
                if iceberg_list[dx][dy] != 0 and check[dx][dy] == 0:
                    check[dx][dy] = 1
                    queue.append([dx, dy])

def ice():
    iceberg_tmp = copy.deepcopy(iceberg)
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:
                for k in range(4):
                    dx = i + nx[k]
                    dy = j + ny[k]
                    if 0 <= dx < n and 0 <= dy < m:
                        if iceberg[dx][dy] == 0:
                            if iceberg[i][j] > 0:
                                iceberg_tmp[i][j] -= 1
                            if iceberg_tmp[i][j] == 0:
                                break


while True:
    iceberg_list = ice()
    iceberg = copy.deepcopy(iceberg_list)
    check = [[0]*m for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(m):
            if iceberg_list[i][j] != 0 and check[i][j] == 0:
                if cnt == 2:
                    print(year)
                bfs(i, j)
                cnt += 1
    year += 1