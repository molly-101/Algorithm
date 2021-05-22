from collections import deque


def solution(arr):
    dq = deque(arr)
    dq.appendleft("+")
    result = 0

    while dq:
        num = int(dq.pop())
        sign = dq.pop()

        if sign == "-":
            if result >= 0:
                result -= num
            else:
                result = -(num + result)
        else:
            result += num

    return result


if __name__ == "__main__":
    arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4", "-", "3"]
    print(solution(arr))