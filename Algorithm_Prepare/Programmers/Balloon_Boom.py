def solution(a):
    stack = []
    mini = a[0]
    if len(a) <= 2:
        return len(a)

    result = 1

    for i in range(1, len(a)):
        if mini > a[i]:
            stack = []
            result += 1
            mini = a[i]
            continue

        if not stack:
            stack.append(a[i])
        else:
            while stack:
                if stack[-1] < a[i]:
                    stack.append(a[i])
                    break
                else:
                    stack.pop()

            if not stack:
                stack.append(a[i])

    return result + len(stack)