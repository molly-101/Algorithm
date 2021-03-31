def solution(n, money):
    memo = [0] * (n + 1)
    memo[0] = 1

    for i in money:
        for j in range(n + 1 - i):
            memo[j + i] += memo[j]
            memo[j + i] %= 1000000007

    return memo[n]


if __name__ == "__main__":
    n = 5
    money = [1,2,5]
    solution(n,money)