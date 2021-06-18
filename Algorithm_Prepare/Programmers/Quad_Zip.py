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

        state = res[0][0]

        for j in res:
            for k in j:
                if k != state:
                    for q in qs:
                        quad_zip(q, result)
                    return
        else:
            result[state] += 1
    else:
        result[res[0][0]] += 1


if __name__ == "__main__":
    arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
    print(solution(arr))