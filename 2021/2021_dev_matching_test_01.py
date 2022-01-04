def solution(lottos, win_nums):
    answer = []
    min = []
    max = []

    ranking = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5
    }

    lotto_list = [lottos[j]
                  for j in range(len(lottos)) if lottos[j] not in win_nums]

    min_value = len(lottos) - len(lotto_list)
    max_value = lotto_list.count(0) + min_value

    if min_value in ranking:
        min.append(ranking[min_value])
    else:
        min.append(6)

    if max_value in ranking:
        max.append(ranking[max_value])
    else:
        max.append(6)

    answer = max + min

    return answer


lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

print(solution(lottos, win_nums))
