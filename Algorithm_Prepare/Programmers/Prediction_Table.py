def solution(n, a, b):
    answer = 0
    while abs(a - b) != 1 or a // 2 == b // 2:
        if a % 2 == 1:
            a += 1
            a //= 2
        else:
            a //= 2

        if b % 2 == 1:
            b += 1
            b //= 2
        else:
            b //= 2
        answer += 1
    return answer + 1