def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        if count_divide(i) % 2 == 0:
            result += i
        else:
            result -= i

    return result


def count_divide(num):
    cnt = 1
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            cnt += 1
    return cnt