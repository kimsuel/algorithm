# 유기농 배추

t = int(input())
result = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0]*n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1

    stack = []
    count = 0

    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                stack.append([i, j])
                while stack:
                    x, y = stack.pop()
                    if field[x][y] == 1:
                        field[x][y] = 0
                    for h in range(4):
                        nx = x + dx[h]
                        ny = y + dy[h]
                        if 0 <= nx < m and 0 <= ny < n:
                            if field[nx][ny] == 1:
                                stack.append([nx, ny])
                count += 1
    result.append(count)

for i in result:
    print(i)
