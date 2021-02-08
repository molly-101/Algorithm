import sys
sys.stdin = open('input.txt','rt')

N = int(input())
res = []
memo = [0]*N  # 밑면, 높이, 무게
result = 0
# res 에 [밑변, 높이, 무게] 순으로 저장
for i in range(N):
    tmp = list(map(int, input().split()))
    res.append(tmp)

# res 를 LIS 로 풀기 위해서 밑면 넓이가 넓은 순으로 정렬한 값을 sort_res 에 저장
sort_res = sorted(res, key= lambda x: x[0], reverse = True)

# memo[0]은 한 눈에 계산이 가능하기 때문에 메모이제이션
memo[0] = sort_res[0][1]

for i in range(1, N):
    maximum = 0
    for j in range(i-1, -1,-1):
        if sort_res[j][2] > sort_res[i][2] and maximum < memo[j]:
            maximum = memo[j]
    memo[i] = maximum + sort_res[i][1]

    if memo[i] > result:
        result = memo[i]
print(result)