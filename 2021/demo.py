def solution(v):
    answer = []
    v1 = []
    v2 = []

    for i in range(len(v)):
        if v[i][0] not in v1:
            v1.append(v[i][0])
        else:
            v1.remove(v[i][0])

        if v[i][1] not in v2:
            v2.append(v[i][1])
        else:
            v2.remove(v[i][1])

    answer = v1 + v2

    return answer


v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))
