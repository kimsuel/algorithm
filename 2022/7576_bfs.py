# 토마토
from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tomato[nx][ny] == 0:
                queue.append([nx, ny])
                tomato[nx][ny] = tomato[x][y] + 1

answer = 0

for i in tomato:
    if 0 in i:
        print(-1)
        exit(0)
    else:
        answer = max(answer, max(i))

print(answer-1)
