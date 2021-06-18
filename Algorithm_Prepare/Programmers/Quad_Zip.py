def solution(arr):
    result = [0, 0]
    quad_zip(arr, result)

    return result


def quad_zip(res, result):
    if len(res) > 1:

        q1 = [i[:len(res) // 2] for i in res[:len(res) // 2]]
        q2 = [i[len(res) // 2:] for i in res[:len(res) // 2]]
        q3 = [i[:len(res) // 2] for i in res[len(res) // 2:]]
        q4 = [i[len(res) // 2:] for i in res[len(res) // 2:]]
        qs = [q1, q2, q3, q4]

        bp = False

        for j in res:
            state = j[0]
            for k in j:
                if k != state:
                    bp = True
                    for q in qs:
                        quad_zip(q, result)
                    break
            if bp:
                break
        else:
            result[state] += 1

    else:
        result[res[0][0]] += 1


if __name__ == "__main__":
    arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
    print(solution(arr))