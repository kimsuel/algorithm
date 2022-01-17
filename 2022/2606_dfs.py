# 바이러스

com = int(input())
n = int(input())
virus = [[] for _ in range(com+1)]

for _ in range(n):
    fromVal, toVal = map(int, input().split())
    virus[fromVal].append(toVal)
    virus[toVal].append(fromVal)

stack = []
visited = []
global count
count = -1


def dfs(k):
    global count
    if k not in visited:
        count += 1
        visited.append(k)
    for i in virus[k]:
        if i not in visited:
            dfs(i)


dfs(1)
print(count)


# stack.append(1)

# while stack:
#     cur = stack.pop()
#     if cur not in visited:
#         count += 1
#         visited.append(cur)
#     for i in virus[cur]:
#         if i not in visited:
#             stack.append(i)

# print(count)
