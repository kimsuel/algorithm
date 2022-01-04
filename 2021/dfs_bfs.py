# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    fromVal, toVal = map(int, input().split())
    graph[fromVal].append(toVal)
    graph[toVal].append(fromVal)

for i in range(1, n+1):
    graph[i].sort()

stack = list()
queue = list()
visited1 = []
visited2 = []
stack.append(v)
queue.append(v)

while stack:
    cur = stack.pop()
    if cur not in visited1:
        print(cur, end=' ')
        visited1.append(cur)
    for j in reversed(graph[cur]):
        if j not in visited1:
            stack.append(j)
print()

while queue:
    cur = queue.pop(0)
    if cur not in visited2:
        print(cur, end=' ')
        visited2.append(cur)
    for j in graph[cur]:
        if j not in visited2:
            queue.append(j)
print()