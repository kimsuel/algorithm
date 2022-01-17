# 벽 부수고 이동하기
from collections import deque

n, m = map(int, input().split())

board = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        x, y, wall = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny][wall] == 0:
                    if board[nx][ny] == 0:
                        queue.append((nx, ny, wall))
                        visited[nx][ny][wall] = visited[x][y][wall] + 1

                    if wall == 0 and board[nx][ny] == 1:
                        queue.append((nx, ny, 1))
                        visited[nx][ny][1] = visited[x][y][wall] + 1
    return -1


print(bfs())
