# 미로탐색 = 2178

n, m = map(int,input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 변수 선언
queue = []
visited = [[0]*m for _ in range(n)]
nx = [0,0,1,-1]
ny = [1,-1,0,0]

queue.append([0, 0])
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)
    if [x, y] == [n-1, m-1]:
        print(visited[x][y])
        break
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        if 0 <= dx < n and 0 <= dy < m:
            if graph[dx][dy] != 0 and visited[dx][dy] == 0:
                visited[dx][dy] = visited[x][y] + 1
                queue.append([dx, dy])


