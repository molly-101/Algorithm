def solution(n):
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    if n < 3:
        return memo[n]
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


if __name__ == "__main__":
    n = 100000
    print(solution(n))