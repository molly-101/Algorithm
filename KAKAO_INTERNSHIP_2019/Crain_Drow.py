def solution(board, moves):
    stack = []
    result = 0

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                if stack and stack[-1] == board[i][move - 1]:
                    stack.pop()
                    result += 2
                else:
                    stack.append(board[i][move - 1])

                board[i][move - 1] = 0
                break

    return result


if __name__ == "__main__":
    moves = [1,5,3,5,1,2,1,4]
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    solution(board, moves)