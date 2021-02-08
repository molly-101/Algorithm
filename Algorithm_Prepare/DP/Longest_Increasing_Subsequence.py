import sys
sys.stdin = open('input.txt','rt')

N = int(input())
res = list(map(int,input().split()))

# 1번부터 시작하기 위해서 0번에 0을 넣어준 것
res.insert(0,0)
memo = [0]*(N+1)
memo[1] = 1
result = 0 # return 될 값 (최종결과값)

# DP Start
# i 번째 항에서 이전 항으로 조건을 만족하는 최대한 많은 LIS를 찾는 과정
for i in range(2,N+1):
    max = 0  # i 에서 가장 많이 이을 수 있는 값을 저장하는 변수
    for j in range(i-1,0,-1):
        if res[i] > res[j] and max < memo[j]:
            max = memo[j]
    memo[i] = max + 1
    if result < memo[i]:
        result = memo[i]
print(result)
