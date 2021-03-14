def solution(number, k):
    stack = []
    rm_cnt = 0
    i = 0

    while i < len(number) and rm_cnt < k:
        if not stack:
            stack.append(number[i])
            i += 1
        else:
            if int(stack[-1]) < int(number[i]):
                stack.pop()
                rm_cnt += 1
            else:
                stack.append(number[i])
                i += 1

    if rm_cnt == k:
        return "".join(stack) + number[i:]
    else:
        return "".join(stack)[:rm_cnt-k]


if __name__ == "__main__":
    number = "9999"
    print(solution(number, 2))