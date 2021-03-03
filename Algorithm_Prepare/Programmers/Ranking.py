def solution(n, results):
    # create board -> inf == no result
    win_board = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    lose_board = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    # a to a = 0
    for i in range(n + 1):
        win_board[i][i] = 0
        lose_board[i][i] = 0

    # input results on board
    for result in results:
        win_board[result[0]][result[1]] = 1
        lose_board[result[1]][result[0]] = 1

    # floyd warshall algorithm
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                win_board[j][k] = min(win_board[j][k], win_board[j][i] + win_board[i][k])
                lose_board[j][k] = min(lose_board[j][k], lose_board[j][i] + lose_board[i][k])

    # return value
    result_cnt = 0

    for i, j in zip(win_board,lose_board):
        game_cnt = 0
        for k, q in zip(i, j):
            if k < 10000000 and k != 0:
                game_cnt += 1
            if q < 10000000 and k != 0:
                game_cnt += 1
        if game_cnt == n-1:
            result_cnt += 1
    return result_cnt


if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))