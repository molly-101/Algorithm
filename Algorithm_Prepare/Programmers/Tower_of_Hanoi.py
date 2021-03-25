def solution(n):
    result = []

    def hanoi(n, fr, to, other):
        if n == 0: return
        hanoi(n-1, fr, other, to)
        result.append([fr, to])
        hanoi(n-1, other, to, fr)

    hanoi(n, 1, 3, 2)

    return result


if __name__ == "__main__":
    n = 2
    print(solution(n))