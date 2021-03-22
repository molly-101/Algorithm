import math


def solution(n, stations, w):
    state = 1
    dist = []
    answer = 0

    for i in stations:
        if state < i - w:
            dist.append(i - w - state)
        state = i + w + 1
    else:
        if n > state:
            dist.append(n - state+1)

    for i in dist:
        answer += math.ceil(i / (2 * w + 1))

    return answer


if __name__ == "__main__":
    n = 15
    stations = [4, 11]
    w = 2
    print(solution(n, stations, w))