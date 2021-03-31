import copy


def solution(n, costs):
    board = [[float('inf')] * n for _ in range(n)]
    costs = sorted(costs, key=lambda x: x[2], reverse=True)
    cost = 0

    for i in costs:
        cost += i[2]

    for i in range(n):
        board[i][i] = 0

    for i in costs:
        board[i[0]][i[1]] = i[2]
        board[i[1]][i[0]] = i[2]
    for i in costs:
        board[i[0]][i[1]] = float('inf')
        board[i[1]][i[0]] = float('inf')

        n_board = copy.deepcopy(board)

        for j in range(n):
            for k in range(n):
                for q in range(n):
                    board[k][q] = min(board[k][q], board[k][j] + board[j][q])

        for j in board[0]:
            if j > 10000000:
                n_board[i[0]][i[1]] = i[2]
                n_board[i[1]][i[0]] = i[2]
                board = n_board
                break
        else:
            board = n_board
            cost -= i[2]

    return cost


if __name__ == "__main__":
    n = 4
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    print(solution(n, costs))