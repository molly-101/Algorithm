def solution(n, k):
    res = [i for i in range(1, n + 1)]
    result = []
    k -= 1

    while n > 0:
        n -= 1
        f = make_factorial(n)
        result.append(res[k // f])
        del res[k // f]
        k = k % f

    return result


def make_factorial(num):
    if num <= 1:
        return 1

    result = 1

    for i in range(1, num + 1):
        result *= i

    return result


if __name__ == "__main__":
    print(solution(3,5))