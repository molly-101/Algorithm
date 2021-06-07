def solution(m, n, board):
    result = 0
    tmp = []
    for i in board:
        tmp.append(list(i))
    board = tmp

    while True:
        for i in range(n):
            for j in range(m - 2, -1, -1):
                for k in range(j, m - 1):
                    if board[k][i] != "O" and board[k + 1][i] == "O":
                        board[k + 1][i] = board[k][i]
                        board[k][i] = "O"

        cnt = findSquare(m, n, board)
        result += cnt
        if cnt == 0:
            return result


def findSquare(m, n, board):
    removed = []
    for i in range(m - 1):
        for j in range(n - 1):
            tmp = board[i][j]
            if tmp == "O":
                continue
            if board[i + 1][j] == tmp and board[i][j + 1] == tmp and board[i + 1][j + 1] == tmp:
                if [i, j] not in removed:
                    removed.append([i,j])
                if [i,j+1] not in removed:
                    removed.append([i,j+1])
                if [i+1,j] not in removed:
                    removed.append([i+1,j])
                if [i+1,j+1] not in removed:
                    removed.append([i+1,j+1])

    rm = len(removed)
    if removed:
        for i in removed:
            board[i[0]][i[1]] = "O"

    return rm


if __name__ == "__main__":
    board = ["AAAAA","AUUUA","AUUAA","AAAAA"]
    m = 4
    n = 5
    a = set()
    a.update(((0,1), 1))
    print(solution(m, n, board))