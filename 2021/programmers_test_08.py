# 오픈채팅방

# 틀림
# def solution(record):
#     global answer
#     global enter_txt
#     global leave_txt
#     global userId

#     answer = []
#     enter_txt = '님이 들어왔습니다.'
#     leave_txt = '님이 나갔습니다.'
#     userId = []

#     for re in record:
#         user_info = re.split(' ')
#         if user_info[0] == 'Enter':
#             answer.append(user_info[2] + enter_txt)
#             check(user_info[1], user_info[2], record)
#             userId.append(user_info[1])
#         elif user_info[0] == 'Leave':
#             if user_info[1] in userId:
#                 user = record[userId.index(user_info[1])].split(' ')[2]
#                 answer.append(user + leave_txt)
#                 userId.append(user_info[1])
#         elif user_info[0] == 'Change':
#             check(user_info[1], user_info[2], record)

#     return answer


# def check(user_info1, user_info2, record):
#     if user_info1 in userId:
#         res_list = list(
#             filter(lambda x: userId[x] == user_info1, range(len(userId))))
#         for res in res_list:
#             answer[res] = user_info2 + (enter_txt if record[res].split(
#                 ' ')[0] == 'Enter' else leave_txt)


def solution(record):
    answer = []
    dic = {}

    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]

    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' % dic[sentence_split[1]])
        elif sentence_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' % dic[sentence_split[1]])

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

print(solution(record))
