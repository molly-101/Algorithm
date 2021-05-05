from itertools import permutations


def solution(expression):
    # make expression to array : res
    res = makeArrayExpression(expression)

    # make *, -, + permutations
    exp = ["*", "-", "+"]
    permutationExp = permutations(exp)

    # find result
    result = 0

    for segmentation in permutationExp:
        copyRes = res
        for seg in segmentation:
            stack = []
            state = False
            for i in copyRes:
                if state:
                    stack.append(returnExpValue(int(stack.pop()),int(i), seg))
                    state = False
                    continue

                if i == seg:
                    state = True
                else:
                    stack.append(i)

            copyRes = stack

        result = max(result, abs(int(copyRes[0])))

    return result


def returnExpValue(v1, v2, e):
    if e == "+":
        return str(v1+v2)
    elif e == "-":
        return str(v1-v2)
    else:
        return str(v1*v2)


def makeArrayExpression(expression):
    res = []
    tmp = ""
    for i in expression:
        if i.isdigit():
            tmp += i
        else:
            res.append(tmp)
            res.append(i)
            tmp = ""
    res.append(tmp)
    return res


if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))