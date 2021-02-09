import sys
sys.stdin = open('input.txt','rt')


if __name__ == "__main__":
    coin_variation = int(input())
    coins = list(map(int,input().split()))
    exchange = int(input())

    memo = [100]*(exchange+1)
    memo[0] = 0
    for i in coins:
        for j in range(i,exchange+1, i):
            memo[j] = min(memo[j], memo[j-i]+1)

    print(memo[exchange])