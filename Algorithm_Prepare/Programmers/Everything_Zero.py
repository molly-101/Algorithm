import sys
sys.setrecursionlimit(300000)


def solution(a, edges):
    tree = [[] for _ in range(len(a))]
    memo = [True] * len(a)
    memo[0] = False

    # make tree's nodes
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    # travel tree's node
    count = [0]
    DFS(0, tree, memo, count, a)

    # return answer
    if a[0] == 0:
        return count[0]
    else:
        return -1


def DFS(level, tree, memo, count, a):
    for node in tree[level]:
        if memo[node]:
            memo[node] = False
            DFS(node, tree, memo, count, a)
            a[level] += a[node]
            count[0] += abs(a[node])


if __name__ == "__main__":
    a = [0,1,0]
    edges = [[0,1],[1,2]]
    print(solution(a, edges))