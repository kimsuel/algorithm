# 바이러스
from collections import deque

com = int(input())
n = int(input())
virus = [[] for _ in range(com+1)]

for _ in range(n):
    fromVal, toVal = map(int, input().split())
    virus[fromVal].append(toVal)
    virus[toVal].append(fromVal)

queue = deque()
visited = []
global count
count = -1

queue.append(1)

while queue:
    cur = queue.popleft()
    if cur not in visited:
        count += 1
        visited.append(cur)
    for i in virus[cur]:
        if i not in visited:
            queue.append(i)

print(count)
