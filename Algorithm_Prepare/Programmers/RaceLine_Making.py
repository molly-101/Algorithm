from collections import deque

# 카카오 2020 하계 인턴십 문제
def solution(board):
    m_board = [[float('inf')] * len(board) for _ in range(len(board))]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    Q = deque()
    Q.append([0, 0, 0, 0])  # 0 누움 1 일어섬
    Q.append([0, 0, 1, 0])
    # BFS 알고리즘을 사용하여 저장
    while Q:
        tmp = Q.popleft()
        for i in range(4):
            tmpx, tmpy = tmp[0] + dx[i], tmp[1] + dy[i]
            if tmp[2] == 0 and i % 2 == 0:
                state, point = 1, tmp[3] + 600
            elif tmp[2] == 1 and i % 2 == 1:
                state, point = 0, tmp[3] + 600
            else:
                state, point = tmp[2], tmp[3] + 100

            if 0 <= tmpx < len(board) and 0 <= tmpy < len(board) and m_board[tmpx][tmpy] >= point and board[tmpx][tmpy] == 0:
                Q.append([tmpx, tmpy, state, point])
                m_board[tmpx][tmpy] = point

    print(m_board)
    return m_board[len(board) - 1][len(board) - 1]


if __name__ == "__main__":
    board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
    solution(board)