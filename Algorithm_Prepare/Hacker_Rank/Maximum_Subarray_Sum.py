import sys
sys.stdin = open('input.txt','rt')


def maximumSum(a, m):
    s = 0
    modular_sum_list = []

    # logic 1. 연속된 부분행렬 이므로 정렬해도 위치를 잃지 않기 위해서 index 와 modular 연산된 sum 값을 리스트에 저장
    for i in range(len(a)):
        s = (s+a[i]%m)%m
        if s == m-1: return s
        modular_sum_list.append([i,s])

    # logic 2. modular된 sum 값이 작은 순서부터 정렬
    modular_sum_list = sorted(modular_sum_list, key=lambda x:x[1])

    min_d = m  # Key Point: minimum distance 즉, 자기 자신보다 큰 modular sum 값을 기준으로 가장 적게 떨어져 있는 값을 찾아넣는다.
    max_s = 0  # 루프를 돌아 실질적으로 들어가게 될 결과

    for i in range(len(modular_sum_list)-1):
        if 0< modular_sum_list[i+1][1] - modular_sum_list[i][1] < min_d and modular_sum_list[i][0] > modular_sum_list[i+1][0]:
            min_d = modular_sum_list[i+1][1] - modular_sum_list[i][1]
            max_s = modular_sum_list[i][1] - modular_sum_list[i+1][1] + m

    return max(max_s, modular_sum_list[-1][1])



if __name__ == "__main__":
    m = 1399760164
    a = list(map(int, input().split()))
    print(maximumSum(a,m))
