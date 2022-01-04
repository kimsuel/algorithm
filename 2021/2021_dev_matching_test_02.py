def solution(rows, columns, queries):
    answer = []

    metrix = [[0]*columns for _ in range(rows)]

    cnt = 0
    for i in range(rows):
        for j in range(columns):
            cnt += 1
            metrix[i][j] = cnt

    for x1, y1, x2, y2 in queries:
        tmp = metrix[x1-1][y1-1]
        mini = tmp

        for k in range(x1-1, x2-1):  # 왼쪽 세로
            num = metrix[k+1][y1-1]
            metrix[k][y1-1] = num
            mini = min(mini, num)

        for k in range(y1-1, y2-1):
            num = metrix[x2-1][k+1]
            metrix[x2-1][k] = num
            mini = min(mini, num)  # 하단 가로

        for k in range(x2-1, x1-1, -1):  # 오른쪽 세로
            num = metrix[k-1][y2-1]
            metrix[k][y2-1] = num
            mini = min(mini, num)

        for k in range(y2-1, y1-1, -1):  # 상단 가로
            num = metrix[x1-1][k-1]
            metrix[x1-1][k] = num
            mini = min(mini, num)

        metrix[x1-1][y1] = tmp
        answer.append(mini)

    return answer


rows = 100
columns = 97
queries = [[1, 1, 100, 97]]

print(solution(rows, columns, queries))
