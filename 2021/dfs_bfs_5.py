# 빙산

import copy

n, m = map(int, input().split())

iceberg = [list(map(int, input().split())) for _ in range(n)]
iceberg_tmp = copy.deepcopy(iceberg)

queue = []
nx = [0, 1, 0, -1]
ny = [1, 0, -1, 0]
result_count = 0

def dfs():
    global iceberg
    visited = []
    count = 0
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0 and [i, j] not in visited:
                queue.append([i, j])
                count += 1
                if (count > 1):
                    break
                while queue:
                    x, y = queue.pop(0)
                    visited.append([x, y])
                    for k in range(4):
                        dx = x + nx[k]
                        dy = y + ny[k]
                        if 0 <= dx < n and 0 <= dy < m:
                            if iceberg[dx][dy] != 0 and [dx, dy] not in visited:
                                queue.append([dx, dy])
    if (count == 1):
        iceberg_dfs()

def iceberg_dfs():
    global result_count
    global iceberg
    global iceberg_tmp
    result_count += 1
    
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
                            if iceberg_tmp[i][j] < 0:
                                iceberg_tmp[i][j] = 0
    iceberg = copy.deepcopy(iceberg_tmp)
    dfs()

iceberg_dfs()

print(result_count)