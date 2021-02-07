import sys
#sys.stdin = open('input.txt','rt')


def DFS(N):
    if memo[N] > 0:
        return memo[N]
    if N == 1 or N == 2:
        return N
    else:
        memo[N] = DFS(N-2) + DFS(N-1)
        return memo[N]


if __name__ == "__main__":
    N = int(input())
    memo = [0]*(N+1)
    print(DFS(N))
