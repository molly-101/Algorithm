def solution(k):
    word = [0]*(k+1)
    sword = [0]*8
    sword[2], sword[3], sword[4], sword[5], sword[6], sword[7] = 1,1,2,5,6,12

    # k 가 6일때는 0만 있는 경우가 생기기 때문에 즉시 리턴
    if k == 6:
        return 7

    # 백트래킹을 이용한 DP 풀이 : 맨 마지막 segment (무조건 한 숫자) 에 대해서 왼쪽으로 k-x 만큼 성냥개비가
    # 있을때까지 계속해서 탐색한다.
    def DFS(k):
        if k < 0:
            return 0
        if word[k] != 0:
            return word[k]
        if k <= 7:
            return sword[k]
        else:
            word[k] = DFS(k-2) + DFS(k-3) + DFS(k-4) + DFS(k-5)*3 + DFS(k-6)*3 + DFS(k-7)
            return word[k]
    return DFS(k)


if __name__ == "__main__":
    r = [1,4,11, 25, 50]
    for i in r:
        print(solution(i))