def solution(rectangles):
    answer = []
    mx = 0
    my = 0
    for x1, y2, x2, y2 in rectangles:
        if mx < x2:
            mx = x2
        if my < y2:
            my = y2

    return answer


rectangles = [[0, 2, 1, 3], [1, 2, 2, 5], [3, 3, 4, 4], [
    4, 1, 6, 3], [1, 6, 5, 7], [5, 5, 7, 6], [5, 8, 6, 10]]
print(solution(rectangles))
