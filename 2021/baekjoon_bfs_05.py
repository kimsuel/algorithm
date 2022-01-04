# 1389
# 케빈 베이컨의 6단계 법칙

from collections import deque

n, m = map(int, input().split())
relationship = [[] for _ in range(n+1)]
counts = []

for _ in range(m):
    a, b = map(int, input().split())
    relationship[a].append(b)
    relationship[b].append(a)


for i in range(n):
    queue = deque()
    visited = [i+1]
    queue.append(i+1)
    relation_cnt = [0]*(n+1)

    while queue:
        cur = queue.popleft()

        for k in relationship[cur]:
            if k not in visited:
                relation_cnt[k] = relation_cnt[cur] + 1
                visited.append(k)
                queue.append(k)
    counts.append(sum(relation_cnt))

print(counts.index(min(counts))+1)
