def solution(a):
    memo = {}
    res = []
    result = 0

    for i in a:
        if i not in memo:
            memo[i] = 1
        else:
            memo[i] += 1

    for i in memo.keys():
        res.append([i, memo[i]])
    res = sorted(res, key=lambda x: x[1], reverse=True)

    for i in res:
        if result // 2 < memo[i[0]]:
            stack = []
            tmp = []
            for j in a:
                if not tmp:
                    tmp.append(j)
                else:
                    if (tmp[-1] == i[0] and tmp[-1] != j) or (tmp[-1] != i[0] and j == i[0]):
                        tmp.append(j)
                        stack.append(tmp)
                        tmp.clear()

            result = max(result, len(stack) * 2)
        else:
            break

    return result

if __name__ == "__main__":
    a = [0,3,3,0,7,2,0,2,2,0]
    print(solution(a))