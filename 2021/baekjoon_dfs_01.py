# 2606

computer = int(input())
n = int(input())
network = [[] for i in range(computer+1)]
count = 0

for _ in range(n):
    fromVal, toVal = map(int, input().split())
    network[fromVal].append(toVal)
    network[toVal].append(fromVal)

for i in range(1, computer+1):
    network[i].sort()

stack = []
visited = []
stack.append(1)


while stack:
    cur = stack.pop()
    if cur not in visited:
        visited.append(cur)
        count += 1
    for j in network[cur]:
        if j not in visited:
            stack.append(j)

print(count-1)

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
