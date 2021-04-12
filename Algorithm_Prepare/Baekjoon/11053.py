import sys
sys.stdin = open('input.txt','rt')


def solution(n, res):
    memo = [0]*n
    memo[0] = 1
    answer = 1

    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if res[i] > res[j]:
                memo[i] = max(memo[j], memo[i])
        memo[i] += 1
        answer = max(answer, memo[i])

    return answer


if __name__ == "__main__":
    n = int(input())
    res = list(map(int,input().split()))
    print(solution(n, res))