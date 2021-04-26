def solution(rows, columns, queries):
    board = [[i for i in range(j * columns + 1, j * columns + columns + 1)] for j in range(0, rows)]
    answer = []

    for querie in queries:
        dx, dy = [querie[0] - 1, querie[2] - 1], [querie[1] - 1, querie[3] - 1]
        before = board[dx[0]][dy[0]]
        minimum = before

        # upside
        for i in range(dy[0] + 1, dy[1] + 1):
            tmp = board[dx[0]][i]
            board[dx[0]][i] = before
            before = tmp
            minimum = min(minimum, tmp)

        # right side
        for i in range(dx[0] + 1, dx[1] + 1):
            tmp = board[i][dy[1]]
            board[i][dy[1]] = before
            before = tmp
            minimum = min(minimum, tmp)

        # bottom side
        for i in range(dy[1]-1, dy[0] - 1, -1):
            tmp = board[dx[1]][i]
            board[dx[1]][i] = before
            before = tmp
            minimum = min(minimum, tmp)

        # left side
        for i in range(dx[1]-1, dx[0] - 1, -1):
            tmp = board[i][dy[0]]
            board[i][dy[0]] = before
            before = tmp
            minimum = min(minimum, tmp)

        answer.append(minimum)

    return answer


if __name__ == "__main__":
    print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))