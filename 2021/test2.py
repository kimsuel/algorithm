def dfs(cur):
    visited1.append(cur)
    print(cur, end=' ')
    for i in graph[cur]:
        if i not in visited1:
            dfs(i)

def bfs(start):
    queue = [start]
    visited2.append(start)
    while queue:
        cur = queue.pop(0)
        print(cur, end=' ')
        for i in graph[cur]:
            if i not in visited2:
                queue.append(i)
                visited2.append(i)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited1 = []
visited2 = []

for _ in range(m):
    fromVal, toVal = map(int, input().split())
    graph[fromVal].append(toVal)
    graph[toVal].append(fromVal)

for i in range(1, n+1):
    graph[i].sort()

dfs(v)
print()
bfs(v)