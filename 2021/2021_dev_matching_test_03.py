def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    organization = dict(zip(enroll, range(len(enroll))))

    for i in range(len(seller)):
        person = seller[i]
        price = amount[i]*100

        while True:
            node_num = organization[person]
            div = price // 10
            answer[node_num] += price - div
            price = div
            person = referral[node_num]
            if person == '-':
                break
            if div == 0:
                break

    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))
