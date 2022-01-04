# 1012
# 맞았는데 처음에 런타임 에러나서
# import sys 안쓰고 재귀 잘 해결해서 한번 더 풀어보기
import sys
sys.setrecursionlimit(10**6)

testcase = int(input())
result = []
nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]


def dfs(x, y, n, m):
    field[x][y] = 0
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        if 0 <= dx < n and 0 <= dy < m:
            if field[dx][dy] == 1:
                dfs(dx, dy, n, m)


for _ in range(testcase):
    m, n, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1

    count = 0
    for i in range(n):  # 8
        for j in range(m):  # 10
            if field[i][j] == 1:
                dfs(i, j, n, m)
                count += 1

    result.append(count)

for res in result:
    print(res)
