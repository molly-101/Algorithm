from collections import deque


def solution(board):
    DLx,DLy = [-1,0,1,0,0,0,1,1],[0,1,0,-1,0,1,1,0]
    DRx,DRy = [-1,0,1,0,-1,-1,0,0],[0,1,0,-1,-1,0,0,-1]
    ULx,ULy = [-1,0,1,0,-1,0,-1,0], [0,1,0,-1,0,0,-1,-1]
    URx,URy = [-1,0,1,0,0,1,0,1], [0,1,0,-1,1,1,0,0]


    cnt = 0
    board_length = len(board)
    nows = deque()
    nows.append([[0,0],[0,1]])
    check_duplicate = [[[0,0],[0,1]]]
    while nows:
        if [[board_length-1,board_length-1],[board_length-2,board_length-1]] in check_duplicate:
            break
        if [[board_length-1,board_length-2],[board_length-1,board_length-1]] in check_duplicate:
            break
        cnt += 1
        for _ in range(len(nows)):
            now = nows.popleft()
            if now[0][0] == now[1][0]: # case:D
                for i in range(8):
                    tmpLx, tmpLy = now[0][0] + DLx[i], now[0][1] + DLy[i]
                    tmpRx, tmpRy = now[1][0] + DRx[i], now[1][1] + DRy[i]

                    # case0 to 3
                    if 0<=tmpLx<board_length and 0<=tmpLy<board_length and 0<=tmpRx<board_length and 0<=tmpRy<board_length and board[tmpLx][tmpLy] == 0 and board[tmpRx][tmpRy] == 0:
                        if 4<= i <=5:
                            if board[now[0][0]-1][now[0][1]] == 0 and board[now[1][0]-1][now[1][1]] == 0:
                                if [[tmpLx,tmpLy],[tmpRx,tmpRy]] not in check_duplicate:
                                    nows.append([[tmpLx,tmpLy],[tmpRx,tmpRy]])
                                    check_duplicate.append([[tmpLx,tmpLy],[tmpRx,tmpRy]])
                        elif 6<=i<=7:
                            if board[now[0][0] + 1][now[0][1]] == 0 and board[now[1][0] + 1][now[1][1]] == 0:
                                if [[tmpLx, tmpLy], [tmpRx, tmpRy]] not in check_duplicate:
                                    nows.append([[tmpLx, tmpLy], [tmpRx, tmpRy]])
                                    check_duplicate.append([[tmpLx, tmpLy], [tmpRx, tmpRy]])
                        else:
                            if [[tmpLx, tmpLy], [tmpRx, tmpRy]] not in check_duplicate:
                                nows.append([[tmpLx, tmpLy], [tmpRx, tmpRy]])
                                check_duplicate.append([[tmpLx, tmpLy], [tmpRx, tmpRy]])

            else: # case:U
                for i in range(8):
                    tmpLx, tmpLy = now[0][0] + ULx[i], now[0][1] + ULy[i]
                    tmpRx, tmpRy = now[1][0] + URx[i], now[1][1] + URy[i]

                    # case0 to 3
                    if 0<=tmpLx<board_length and 0<=tmpLy<board_length and 0<=tmpRx<board_length and 0<=tmpRy<board_length and board[tmpLx][tmpLy] == 0 and board[tmpRx][tmpRy] == 0:
                        if 4<= i <=5:
                            if board[now[0][0]][now[0][1]+1] == 0 and board[now[1][0]][now[1][1]+1] == 0:
                                if [[tmpLx, tmpLy], [tmpRx, tmpRy]] not in check_duplicate:
                                    nows.append([[tmpLx, tmpLy], [tmpRx, tmpRy]])
                                    check_duplicate.append([[tmpLx, tmpLy], [tmpRx, tmpRy]])
                        elif 6<=i<=7:
                            if board[now[0][0]][now[0][1]-1] == 0 and board[now[1][0]][now[1][1]-1] == 0:
                                if [[tmpLx, tmpLy], [tmpRx, tmpRy]] not in check_duplicate:
                                    nows.append([[tmpLx, tmpLy], [tmpRx, tmpRy]])
                                    check_duplicate.append([[tmpLx, tmpLy], [tmpRx, tmpRy]])
                        else:
                            if [[tmpLx, tmpLy], [tmpRx, tmpRy]] not in check_duplicate:
                                nows.append([[tmpLx, tmpLy], [tmpRx, tmpRy]])
                                check_duplicate.append([[tmpLx, tmpLy], [tmpRx, tmpRy]])
    return cnt


if __name__ == "__main__":
    board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
    print(solution(board))