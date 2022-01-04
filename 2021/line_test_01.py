def solution(record):
    answer = []
    activity_list = []
    money_list = []
    count_list = []
    for rec in record:
        num = rec.split(' ')
        activity_list.append(num[0])
        money_list.append(num[1])
        count_list.append(num[2])

    answer.append(first(activity_list, money_list, count_list))
    answer.append(last(activity_list, money_list, count_list))

    return answer


def first(activity, money, count):
    s_count = 0
    result = 0
    for i in range(len(activity)):
        if activity[i] == 'S':
            s_count += int(count[i])

    for i in range(len(activity)):
        if activity[i] == 'P':
            if s_count <= int(count[i]):
                result += s_count * int(money[i])
                break
            else:
                result += int(count[i]) * int(money[i])
                s_count -= int(count[i])

    return result


def last(activity, money, count):
    s_count = 0
    result = 0
    for i in range(len(activity)):
        if activity[i] == 'S':
            s_count = int(count[i])
            for j in range(i, 0, -1):
                if activity[j-1] == 'P':
                    if s_count <= int(count[j-1]):
                        result += s_count * int(money[j-1])
                        count[j-1] = int(count[j-1]) - int(s_count)
                        break
                    else:
                        result += int(count[j-1]) * int(money[j-1])
                        s_count -= int(count[j-1])
                        count[j-1] = 0

    return result


# record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]
# record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]
record = ["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"]
print(solution(record))
