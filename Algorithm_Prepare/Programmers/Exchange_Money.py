def solution(n, money):
    memo = [0]*(n+1)

    def back_tracking(n):
        if n < 0:
            return 0
        if memo[n] != 0:
            return memo[n]
        if n == 0:
            return 1
        else:
            memo[n] = sum(back_tracking(n-i) for i in money)
            return memo[n]
    print(back_tracking(n))


if __name__ == "__main__":
    n = 5
    money = [1,2,5]
    solution(n,money)