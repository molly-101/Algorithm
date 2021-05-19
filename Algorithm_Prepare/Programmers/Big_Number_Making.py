def solution(number, k):
    stack = []

    for i in range(len(number)):
        if stack:
            while stack and int(number[i]) > int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1

        if k == 0:
            return "".join(stack) + number[i:]
        else:
            stack.append(number[i])

    if k > 0:
        stack = stack[:-k]

    return "".join(stack)


if __name__ == "__main__":
    number = "4177252841"
    k = 4

    print(solution(number, k))