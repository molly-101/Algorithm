import sys
sys.stdin = open('input.txt','rt')

N = int(input())
right = list(map(int,input().split()))
memo = [[0,0]]*(N+1)  # 위치, 자신 포함 이전까지의 이어질 수 있는 선 개수
result = 0

for i in range(1, N+1):
    max_connection = 0
    for k in range(N):
        if right[k] == i:
            for j in range(i-1,0,-1):
                if memo[j][0] < k and max_connection < memo[j][1]:
                    max_connection = memo[j][1]
            memo[i] = [k, max_connection+1]
            break

    if result < memo[i][1]:
        result = memo[i][1]
print(result)