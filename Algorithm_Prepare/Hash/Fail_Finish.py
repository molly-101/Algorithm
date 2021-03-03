def solution(participant, completion):
    finish = {}
    for man in participant:
        if man not in finish:
            finish[man] = 1
        else:
            finish[man] += 1

    for man in completion:
        if finish[man] == 1:
            del finish[man]
        else:
            finish[man] -= 1

    return "".join(list(finish.keys()))