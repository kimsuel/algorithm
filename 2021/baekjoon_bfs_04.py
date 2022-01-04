# 14716
# 현수막

from collections import deque

m, n = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

count = 0
for i in range(m):
    for j in range(n):
        if banner[i][j] == 1:
            queue = deque()
            queue.append([i, j])
            banner[i][j] = 0

            while queue:
                x, y = queue.popleft()
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n:
                        if banner[nx][ny] == 1:
                            queue.append([nx, ny])
                            banner[nx][ny] = 0
            count += 1

print(count)
