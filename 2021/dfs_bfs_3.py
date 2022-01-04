#보물섬
from collections import deque

r, c = map(int, input().split())

island = [list(map(str, input())) for _ in range(r)]
result = 0

for i in range(r):
    for j in range(c):
        if island[i][j] == 'L':
            queue = deque()
            visited = []
            queue.append([i,j])
            count = 0
            while queue:
                x, y = queue.popleft()
                visited.append([x, y])
                xy_list = [[x, y-1], [x+1, y], [x, y+1], [x-1, y]]
                for dx, dy in xy_list:
                    if ((dx >= 0 and dx < r) and (dy >= 0 and dy < c)):
                        if([dx, dy] not in visited):
                            if (island[dx][dy] == 'L'):
                                queue.append([dx, dy])
                                count += 1
            if (result == 0 or result > count):
                result = count

print(result)
                    
