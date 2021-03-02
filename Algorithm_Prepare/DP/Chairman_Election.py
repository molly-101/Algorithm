import sys
sys.stdin = open('input.txt','rt')


if __name__ == "__main__":
    # 인원 수 넣어준다
    n = int(input())

    # 전체 거리는 최대로 설정
    board = [[1000]*(n+1) for _ in range(n+1)]

    # 자기 자신에서 자기 자신으로 가는 경우에는 0
    for i in range(n+1):
        board[i][i] = 0

    # input 값으로 주어지는 a to b 간선들을 1로 표현 (친구)
    while True:
        a, b = map(int, input().split())
        if a == -1:
            break
        else:
            board[a][b] = 1
            board[b][a] = 1

    # floyd warshall algorithm
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                # j to k 직행과 i 를 거쳐 가는 것 중 보다 빠른 경로를 넣어준다.
                board[j][k] = min(board[j][k], board[j][i] + board[i][k])

    chairman = []
    point = float('inf')
    # 회장 후보들을 선별
    for i in range(1,n+1):
        max_point = max(board[i][1:])
        if max_point < point:
            chairman = []
            chairman.append(i)
            point = max_point
        elif max_point == point:
            chairman.append(i)

    print(point, len(chairman))
    print(chairman)