answer = 0


def solution(n):
    global answer
    board = [[0]*n for _ in range(n)]
    DFS(0, board, {},{}, n)

    return answer


# duple down -> , duple up <-
def DFS(col, board, duple_down, duple_up, n):
    global answer

    if col == n:
        answer += 1
        return

    # row move
    for i in range(n):
        if 1 not in board[i][:col] and i-col not in duple_down and i+col not in duple_up:
            board[i][col] = 1
            duple_up[i+col] = 1
            duple_down[i-col] = 1
            DFS(col+1, board, duple_down, duple_up, n)
            board[i][col] = 0
            del duple_up[i+col]
            del duple_down[i-col]


if __name__ == "__main__":
    n = 12
    print(solution(n))