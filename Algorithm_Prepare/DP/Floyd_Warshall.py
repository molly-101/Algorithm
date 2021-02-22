import sys
sys.stdin = open('input.txt','rt')


if __name__ == "__main__":
    city, load = map(int,input().split())
    board = [[5000]*(city+1) for _ in range(city+1)]


    # city i to city i => 0
    for i in range(city+1):
        board[i][i] = 0

    # city a to b by load
    for i in range(load):
        a, b, cost = map(int,input().split())
        board[a][b] = cost

    for i in board:
        for j in i:
            if j == 5000:
                print("M", end=' ')
            else:
                print(j, end=' ')
        print()
    print()
    
    # floyd warshall algorithm
    for i in range(1, city+1):  # i 를 거쳐가야 한다.
        for j in range(1, city+1):  # j city 에서
            for k in range(1, city+1):  #k city까지
                board[j][k] = min(board[j][k], board[j][i] + board[i][k])

    for i in board:
        for j in i:
            if j == 5000:
                print("M", end=' ')
            else:
                print(j, end=' ')
        print()
