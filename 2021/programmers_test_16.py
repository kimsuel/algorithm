def solution(tickets):
    answer = []
    routes = {}

    for ticket in tickets:
        routes.setdefault(ticket[0], []).append(ticket[1])

    for i in routes.keys():
        routes[i].sort(reverse=True)

    stack = ['ICN']

    while stack:
        target = stack[-1]
        if target not in routes or len(routes[target]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[target].pop())

    return answer[::-1]


# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

print(solution(tickets))
