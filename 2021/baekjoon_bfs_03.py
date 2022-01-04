# 2665
# 미로 만들기
from collections import deque

n = int(input())

room = [list(map(int, input())) for _ in range(n)]
ch = [[-1]*n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque()
    queue.append([0, 0])
    ch[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if ch[nx][ny] == -1:
                    if room[nx][ny] == 0:
                        ch[nx][ny] = ch[x][y] + 1
                        queue.append([nx, ny])
                    else:
                        ch[nx][ny] = ch[x][y]
                        queue.appendleft([nx, ny])


bfs()
print(ch[n-1][n-1])
