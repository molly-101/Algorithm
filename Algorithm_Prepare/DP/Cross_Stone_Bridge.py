import sys
sys.stdin = open('input.txt','rt')

N = int(input())
memo = [0]*(N+2)
# Bottom Up 이기 때문에 아주 점화식에서 아주 작은 단계를 미리 메모이제이션 해둔다
memo[1] = 1
memo[2] = 2

for i in range(3,N+2):
    # 점화식
    memo[i] = memo[i-1] + memo[i-2]

print(memo[N+1])