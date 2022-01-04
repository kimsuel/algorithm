def solution(macaron):
    answer = []
    game = [[0]*6 for _ in range(6)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for location, color in macaron:
        for i in range(5, 0, -1):
            if game[i][location-1] == 0:
                game[i][location-1] = color
                break

        print(game)

        # while True:
        #     for i in range(4):
        #         nx = i + dx[i]
        #         ny = location + dy[i]
        #         if ((nx >= 0 and nx < 6) and (ny >= 0 and ny < 6)):
        #             if game[nx][ny] != 0 and

    return answer


macaron = [[1, 1], [2, 1], [1, 2], [3, 3], [
    6, 4], [3, 1], [3, 3], [3, 3], [3, 4], [2, 1]]
print(solution(macaron))
