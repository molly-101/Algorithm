import sys
sys.stdin = open('input.txt','rt')


def solution(n, res):
    memo = [0]*n
    memo[0] = res[0]
    answer = memo[0]

    if n == 1:
        return answer

    for i in range(1, n):
        memo[i] = max(memo[i-1]+res[i], res[i])
        answer = max(memo[i], answer)

    return answer


if __name__ == "__main__":
    n = int(input())
    res = list(map(int,input().split()))
    print(solution(n, res))