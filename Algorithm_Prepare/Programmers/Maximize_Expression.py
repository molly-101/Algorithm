from itertools import permutations
import copy

def solution(expression):
    exp_list = []
    tools = set()  # save +, -, *
    temp = ""

    # 1. list화 해주기
    for e in expression:
        if e.isdigit():
            temp += e
        else:
            exp_list.append(temp)
            temp = ""
            exp_list.append(e)
            tools.add(e)
    else:
        exp_list.append(temp)

    answer = 0

    # 2. permutations of tools
    for order in permutations(tools):
        copy_list = copy.deepcopy(exp_list)

        for i in order:
            copy_list = ordered_value(i, copy_list)
        answer = max(abs(int(copy_list[0])), answer)

    return answer


def ordered_value(order, copy_list):
    tmp = []
    state = ""
    for i in copy_list:
        if state == "-":
            tmp.pop()
            tmp.append(str(int(tmp.pop()) - int(i)))
            state = ""
        elif state == "+":
            tmp.pop()
            tmp.append(str(int(tmp.pop()) + int(i)))
            state = ""
        elif state == "*":
            tmp.pop()
            tmp.append(str(int(tmp.pop()) * int(i)))
            state = ""
        else:
            if order == i:
                state = order
            tmp.append(i)
    return tmp


if __name__ == "__main__":
    expression = "50*6-3*2"
    print(solution(expression))