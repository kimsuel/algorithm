from collections import Counter


def solution(id_list, k):
    answer = 0
    day_list = {}
    count_list = {}
    for idx, id in enumerate(id_list):
        users = set(id.split(" "))
        for i in users:
            count_list[i] = count_list.get(i, 0) + 1
            if (count_list.get(i) <= k):
                day_list.setdefault(idx, []).append(i)

    answer = sum([len(day_list[x])
                 for x in day_list if isinstance(day_list[x], list)])

    return answer


# id_list = ["A B C D", "A D", "A B D", "B D"]
id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY",
           "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
# k = 2
k = 3

print(solution(id_list, k))
