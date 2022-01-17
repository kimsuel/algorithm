# 연결 요소의 개수

import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
elements = [[] for _ in range(n+1)]
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    elements[x].append(y)
    elements[y].append(x)

visited = []
count = 0


def dfs(k):
    visited.append(k)
    for j in elements[k]:
        if j not in visited:
            dfs(j)


for i in range(1, n+1):
    if i not in visited:
        dfs(i)
        count += 1

print(count)
