def solution(arr):
    answer = 0
    result = []
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            result.append('up')
        elif arr[i] == arr[i+1]:
            result.append('same')
        else:
            result.append('down')

    answer = compare(result)

    return answer


def compare(result):
    count = 0
    k = 0
    for i in range(len(result)-1):
        up_count = 0
        down_count = 0
        if result[i] == 'up' and result[i+1] == 'down':
            count += 1
            for j in range(i, k, -1):
                if result[j-1] == 'up':
                    count += 1
                    up_count += 1
                else:
                    break
            for j in range(i+1, len(result)-1):
                if result[j+1] == 'down':
                    count += 1
                    down_count += 1
                else:
                    break
            k = i
            if up_count > 0 and down_count > 0:
                count += min(up_count, down_count)
    return count % (10**9 + 7)


arr = [0, 1, 2, 5, 3, 7]  # 3
# arr = [1, 2, 3, 2, 1]  # 4
# arr = [1, 2, 3, 2, 1, 4, 3, 2, 2, 1]  # 6
# arr = [1, 2, 1, 2, 1]  # 2
print(solution(arr))

# up up up down up
# up up down down
# up up down down up down down same down
# up down up down
