import sys
sys.stdin = open('input.txt','rt')


if __name__ == "__main__":
    N, M = map(int,input().split())
    memo = [0]*(M+1)

    for i in range(N):
        point, time = map(int,input().split())
        for j in range(M,time-1,-1):
            if memo[j] < memo[j-time] + point:
                memo[j] = memo[j-time] + point
    print(memo)