def solution(n):
    memo = [0] * (n + 2)
    memo[1] = 1
    memo[2] = 2

    if n <= 2:
        return memo[n]

    for i in range(3, n + 1):
        memo[i] = memo[i - 2] + memo[i - 1]

    return memo[n] % 1234567