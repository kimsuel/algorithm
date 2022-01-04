# 11724
# 연결 요소의 개수
import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())

element = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

count = 0

for _ in range(m):
    u, v = map(int, input().split())
    element[u].append(v)
    element[v].append(u)


def dfs(start):
    visited[start] = True

    for i in element[start]:
        if not visited[i]:
            dfs(i)


for i in range(n):
    if not visited[i+1]:
        count += 1
        dfs(i+1)


print(count)
