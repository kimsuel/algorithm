import sys
sys.setrecursionlimit(10000)
# recursion 크기 조절 (백준은 1000인가 그럼)

M, N, K = map(int, input().split())

mnMap = [[0]*(N) for _ in range(M)]
square = [[] for _ in range(K)]

result = []
curResult = 0


def dfs(y, x):
    global curResult
    mnMap[y][x] = 1
    curResult += 1
    if (y+1) < M and mnMap[y+1][x] == 0:
        dfs(y+1, x)
    if (x+1) < N and mnMap[y][x+1] == 0:
        dfs(y, x+1)
    if (y-1) >= 0 and mnMap[y-1][x] == 0:
        dfs(y-1, x)
    if (x-1) >= 0 and mnMap[y][x-1] == 0:
        dfs(y, x-1)


for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    square[i].append(x1)
    square[i].append(y1)
    square[i].append(x2)
    square[i].append(y2)

# 전체 사각형 색칠하기
for item in square:
    startX = item[0]
    startY = item[1]
    endX = item[2]
    endY = item[3]
    for y in range(startY, endY):
        for x in range(startX, endX):
            mnMap[y][x] = 1

# bfs/dfs로 너비 찾으면서 색칠하기
# 마지막엔 공간 너비 저장하기
for y in range(M):
    for x in range(N):
        if mnMap[y][x] == 0:
            curResult = 0
            dfs(y, x)
            result.append(curResult)


# sort
result.sort()

print(len(result))
for item in result:
    print(item, end=' ')