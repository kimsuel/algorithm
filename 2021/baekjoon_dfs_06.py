# 1967
# 트리의 지름

import sys
sys.setrecursionlimit(10**6)

n = int(input())

tree = [[] for _ in range(n+1)]
result = [-1]*(n+1)
result[1] = 0


def dfs(node, weight):
    for i in tree[node]:
        n, w = i
        if result[n] == -1:
            result[n] = weight + w
            dfs(n, weight + w)


for _ in range(n-1):
    p_node, c_node, w = map(int, input().split())
    tree[p_node].append((c_node, w))
    tree[c_node].append((p_node, w))

dfs(1, 0)


start = result.index(max(result))
result = [-1]*(n+1)
result[start] = 0
dfs(start, 0)

print(max(result))
