# 11725
# 트리의 부모 찾기

# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = [1 for _ in range(n+1)]


def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            answer[i] = node
            dfs(i)
    return


for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)

for i in range(2, len(answer)):
    print(answer[i])
