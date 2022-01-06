# 촌수계산
import sys
sys.setrecursionlimit(10**9)

n = int(input())
dx, dy = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n+1)]
count = [0 for _ in range(n+1)]
visited = []

for _ in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)


def dfs(x):
    if x not in visited:
        visited.append(x)
    for i in relation[x]:
        if i not in visited:
            count[i] = count[x] + 1
            dfs(i)


dfs(dx)

print(-1 if count[dy] == 0 else count[dy])
