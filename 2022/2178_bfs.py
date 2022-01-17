# 미로 탐색

from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

queue = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
miro_count = [[0]*m for _ in range(n)]
queue.append([0, 0])
miro_count[0][0] = 1

while queue:
    x, y = queue.popleft()
    if x == n-1 and y == m-1:
        print(miro_count[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if miro[nx][ny] != 0 and miro_count[nx][ny] == 0:
                miro_count[nx][ny] = miro_count[x][y] + 1
                queue.append([nx, ny])
