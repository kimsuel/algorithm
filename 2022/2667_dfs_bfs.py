# 단지번호붙이기

n = int(input())

danzi = [list(map(int, input())) for _ in range(n)]

stack = []
cnt_list = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(n):
        if danzi[i][j] == 1:
            stack.append([i, j])
            cur_count = 0
            while stack:
                x, y = stack.pop()
                if danzi[x][y] == 1:
                    danzi[x][y] = 0
                    cur_count += 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if danzi[nx][ny] != 0:
                                stack.append([nx, ny])
            cnt_list.append(cur_count)

cnt_list.sort()
print(len(cnt_list))
for cnt in cnt_list:
    print(cnt)
