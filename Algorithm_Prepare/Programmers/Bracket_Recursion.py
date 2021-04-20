from collections import deque


def solution(s):
    res = deque(s)
    answer = 0

    for i in range(len(s)):
        res.append(res.popleft())
        if check(res):
            answer += 1

    return answer


def check(res):
    stack = []
    for i in res:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == "[" and i == "]":
                stack.pop()
            elif stack[-1] == "{" and i == "}":
                stack.pop()
            elif stack[-1] == "(" and i == ")":
                stack.pop()
            else:
                stack.append(i)
    if stack:
        return False
    else:
        return True


if __name__ == "__main__":
    s = "[](){}"
    print(solution(s))