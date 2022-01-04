#보물섬

r, c = map(int, input().split())

island = []
result = 0
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(r):
    island.append(list(input()))


def bfs(x, y):
    queue.append([x, y])
    visited = [[0]*c for _ in range(r)]
    visited[x][y] = 1
    count = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((nx >= 0 and nx < r) and (ny >= 0 and ny < c)):
                    if (island[nx][ny] == 'L' and visited[nx][ny] == 0):
                        visited[nx][ny] = visited[x][y] + 1
                        count = max(count, visited[nx][ny])
                        queue.append([nx, ny])
    return count-1

for i in range(r):
    for j in range(c):
        if island[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
