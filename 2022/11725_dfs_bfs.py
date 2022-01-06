# 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**9)

n = int(input())
node = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = [1 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


def dfs(k):
    visited[k] = True
    for i in node[k]:
        if not visited[i]:
            answer[i] = k
            dfs(i)
    return


dfs(1)

for i in range(2, len(answer)):
    print(answer[i])
