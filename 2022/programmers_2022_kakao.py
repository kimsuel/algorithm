# 2022 KAKAO BLIND RECRUITMENT

# 내 풀이 (테스트 케이스 1개 실패)
# def solution(id_list, report, k):
#     answer = []
#     report_users = {}
#     reported_users = {}
#     more_k_reports = []

#     for i in report:
#         user, report_user = i.split()
#         report_users.setdefault(user, []).append(report_user)
#         reported_users.setdefault(report_user, []).append(user)

#     for (key, value), (rkey, rvalue) in zip(report_users.items(), reported_users.items()):
#         report_users[key] = list(set(value))
#         reported_users[rkey] = list(set(rvalue))
#         if len(reported_users[rkey]) >= k:
#             more_k_reports.append(rkey)

#     for i in id_list:
#         count = 0
#         for j in more_k_reports:
#             if i in report_users and j in report_users[i]:
#                 count += 1
#         answer.append(count)

#     return answer

# 풀이 1
# def solution(id_list, report, k):
#     s2i = {}
#     n = len(id_list)
#     s = [set() for _ in range(n)]
#     cnt = [0] * n

#     for i in range(n):
#         s2i[id_list[i]] = i

#     for rep in report:
#         id1, id2 = rep.split()
#         s[s2i[id2]].add(s2i[id1])

#     for i in range(n):
#         if len(s[i]) < k:
#             continue
#         for x in s[i]:
#             cnt[x] += 1

#     return cnt

# 풀이 2
def solution(id_list, report, k):
    answer = []
    a = list(set(report))
    dictionary2 = {name: 0 for name in id_list}
    dictionary = {name: [] for name in id_list}
    for i in a:
        dictionary[i.split()[1]].append(i.split()[0])

    for i in dictionary:
        if len(dictionary[i]) >= k:
            for j in dictionary[i]:
                dictionary2[j] += 1

    for i in dictionary2:
        answer.append(dictionary2[i])

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

print(solution(id_list, report, k))
