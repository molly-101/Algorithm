import copy


def solution(tickets):
    memo = {}
    result = []
    for ticket in tickets:
        tmp = "".join(ticket)
        if tmp not in memo:
            memo[tmp] = 1
        else:
            memo[tmp] += 1

    for i in memo:
        now = ["ICN"]
        if i[:3] == "ICN":
            now.append(i[3:])
            memo[i] -= 1
            DFS(1, tickets, memo, now, result)
            memo[i] += 1
    return sorted(result)[0]


def DFS(level, tickets, memo, now, result):
    if level == len(tickets):
        result.append(copy.deepcopy(now))
    else:
        for ticket in tickets:
            tmp = "".join(ticket)
            if now[-1] == ticket[0] and memo[tmp] > 0:
                memo[tmp] -= 1
                now.append(tmp[3:])
                DFS(level + 1, tickets, memo, now, result)
                memo[tmp] += 1
                now.pop()

