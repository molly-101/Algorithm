def solution(n, t, m, p):
    number = 0
    answer = ""
    l_answer = 0
    now = 0

    while True:
        for i in make_n(number, n):
            if now % m + 1 == p:
                if i >= 10:
                    answer += chr(55+i)
                else:
                    answer += str(i)
                l_answer += 1

            if l_answer == t:
                return answer

            now += 1

        number += 1


# 역순으로 적립된다.
def make_n(number, n):
    rt = []

    while number >= n:
        rt.append(number%n)
        number //= n

    rt.append(number)
    rt.reverse()

    return rt


if __name__ == "__main__":
    n = 16
    t = 16
    m = 2
    p = 2
    print(solution(n,t,m,p))