import sys
sys.stdin = open('input.txt','rt')

n, k = map(int, input().split())
memo = [0]*(k+1)

for i in range(n):
    w, v = map(int,input().split())
    for j in range(k,w-1,-1):
        memo[j] = max(memo[j], memo[j-w] + v)

print(memo[k])