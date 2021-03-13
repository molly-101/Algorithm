def solution(money):
    if len(money) == 3:
        return dynamic(money)
    else:
        start, end = dynamic(money[1:]), dynamic(money[:-1])
        return max(start, end)


def dynamic(money):
    memo = [0] * (len(money))
    memo[0] = money[0]
    memo[1] = max(money[1], memo[0])
    memo[2] = max(money[2] + memo[0], memo[1])

    if len(money) > 3:
        for i in range(3, len(money)):
            if memo[i - 1] > money[i] + memo[i - 2]:
                memo[i] = memo[i - 1]
            else:
                memo[i] = memo[i - 2] + money[i]
        return memo[len(memo) - 1]
    else:
        return memo[2]


if __name__ == "__main__":
    a = [1,2,3,1]
    print(solution(a))
