# dfs와 bfs

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited1 = []
visited2 = []
stack = []
queue = deque()
stack.append(v)
queue.append(v)

while stack:
    cur = stack.pop()
    if cur not in visited1:
        visited1.append(cur)
        print(cur, end=' ')
    for i in reversed(graph[cur]):
        if i not in visited1:
            stack.append(i)

print()

while queue:
    cur = queue.popleft()
    if cur not in visited2:
        visited2.append(cur)
        print(cur, end=' ')
    for i in graph[cur]:
        if i not in visited2:
            queue.append(i)
