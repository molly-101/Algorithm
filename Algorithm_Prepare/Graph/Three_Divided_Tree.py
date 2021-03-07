from itertools import combinations


def solution(n, edges):
    tree_board = [[] for _ in range(n)]
    maximum_divide_size = n//3

    a = combinations([i for i in range(n)], 2)

    for edge in edges:
        tree_board[edge[0]].append(edge[1])
        tree_board[edge[1]].append(edge[0])






if __name__ == "__main__":
    n = 50
    edges = [[0,2],[2,1],[2,4],[3,5],[5,4],[5,7],[7,6],[6,8]]
    solution(n, edges)