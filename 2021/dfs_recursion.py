def dfs(cur):
    visited1.append(cur)
    print(cur, end=' ')
    for item in graph[cur]:
        if item not in visited1:
            dfs(item)


def bfs(start):
    visited2.append(start)
    queue = [start]

    while queue:
        cur = queue.pop(0)
        print(cur, end=' ')
        for item in graph[cur]:
            if item not in visited2:
                queue.append(item)
                visited2.append(item)


N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]
visited1 = []
visited2 = []

for _ in range(M):
    fromVal, toVal = map(int, input().split())
    graph[fromVal].append(toVal)
    graph[toVal].append(fromVal)

for i in range(1, N+1):
    graph[i].sort()

dfs(V)
print()
bfs(V)