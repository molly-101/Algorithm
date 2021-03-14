def solution(N, road, K):
    board = [[float('inf')] * N for _ in range(N)]

    # 자기 자신에서 자기자신으로 가는 경로 = 0
    for i in range(N):
        board[i][i] = 0

    # data insert
    for i in road:
        board[i[0]-1][i[1]-1] = min(i[2], board[i[0]-1][i[1]-1])
        board[i[1]-1][i[0]-1] = min(i[2], board[i[1]-1][i[0]-1])

    # warshall
    for i in range(N):
        for j in range(N):
            for k in range(N):
                board[j][k] = min(board[j][k], board[j][i] + board[i][k])

    # count result
    result = 0
    for i in board[0]:
        if i <= K:
            result += 1

    return result


if __name__ == "__main__":
    N = 5
    road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    K = 3
    print(solution(N,road,K))