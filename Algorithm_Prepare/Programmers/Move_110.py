def solution(s):
    result = []

    for num in s:
        if len(num) < 3:
            result.append(num)
        else:
            result.append(returnNumber(num))

    return result


def returnNumber(num):
    stack = []
    return_string = ""
    state = 0

    for i in range(len(num)):
        if len(stack) < 2:
            stack.append(num[i])
            if num[i] == "0":
                return_string += "".join(stack)
                stack.clear()
        else:
            if num[i] == "0":
                stack.pop()
                stack.pop()
                state += 1
            else:
                stack.append(num[i])

    for i in range(state):
        return_string += "110"
    if stack:
        return_string += "".join(stack)

    return return_string


if __name__ == "__main__":
    s =  ["1011110","01110","101101111010", "0000011100011000", "1111000"]
    print(solution(s))