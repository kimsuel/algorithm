#그림
# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1

# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0


import sys
sys.setrecursionlimit(250000)

n, m = map(int, input().split())
painting = [list(map(int, input().split())) for _ in range(n)]
result = []
count = 0

nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]

def dfs(x, y):
    global count
    painting[x][y] = 0
    count += 1
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        if 0 <= dx < n and 0 <= dy < m:
            if painting[dx][dy] == 1:
                dfs(dx, dy)
    

for i in range(n):
    for j in range(m):
        if painting[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)

if len(result) != 0:
    print(len(result))
    print(max(result))
else:
    print(len(result))
    print(0)



