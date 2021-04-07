import copy


def solution(tickets):
    answer = []
    duple = {}

    # make dictionary tickets
    for ticket in tickets:
        if "".join(ticket) not in duple:
            duple["".join(ticket)] = 1
        else:
            duple["".join(ticket)] += 1

    DFS("ICN", duple, tickets, answer, ["ICN"])

    return sorted(answer)[0]


def DFS(now, duple, tickets, answer, temp):
    if len(temp) == len(tickets)+1:
        answer.append(copy.deepcopy(temp))
    else:
        for ticket in tickets:
            if duple["".join(ticket)] > 0 and ticket[0] == now:
                duple["".join(ticket)] -= 1
                temp.append(ticket[1])
                DFS(ticket[1], duple, tickets, answer, temp)
                duple["".join(ticket)] += 1
                temp.pop()


if __name__ == "__main__":
    tickets = [['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]
    print(solution(tickets))