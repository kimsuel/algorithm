def solution(isAvailable, N, M, H, W):
    answer = 0

    for i in range(4):
        stack = []
        visited = []
        for x, y in zip(N, M):
            if isAvailable[x][y] != 0:
                stack.append([x, y])
                while stack:
                    nx, ny = stack.pop()
                    if [nx, ny] not in visited:
                        visited.append([nx, ny])

    return answer


isAvailable = ["1111", "1011", "1011", "1111"]
# isAvailable = ["111110", "110110", "110110", "111110", "111110"]
n = 4
m = 4
h = 2
w = 3

# n = 5
# m = 6
# h = 3
# w = 4

print(solution(isAvailable, n, m, h, w))


입출력 예 설명
입출력 예  # 1
지문의 4가지 그림 중 위에서부터
첫번째 그림과 같은 방향으로 책상을 놓는 방법의 수가 1가지,
두번째 그림처럼 놓는 방법의 수가 2가지,
세번째 그림처럼 놓는 방법의 수가 1가지,
네번째 그림처럼 놓는 방법의 수가 2가지로 총 6가지입니다.

입출력 예  # 2

위에서부터 첫번째 그림처럼 놓는 방법의 수가 2가지,
두번째 그림처럼 놓는 방법의 수가 2가지,
세번째 그림처럼 놓는 방법의 수가 4가지,
네번째 그림처럼 놓는 방법의 수가 2가지로 총 10가지입니다.
