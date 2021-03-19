def solution(n, works):
    work_dict = {}

    for i in works:
        if i not in work_dict:
            work_dict[i] = 1
        else:
            work_dict[i] += 1

    while n > 0 and work_dict:
        maximum = max(work_dict)
        if work_dict[maximum] > n:
            work_dict[maximum] -= n
            if maximum-1 > 0:
                if maximum-1 not in work_dict:
                    work_dict[maximum-1] = n
                else:
                    work_dict[maximum-1] += n
            n -= n

        else:
            if maximum - 1 > 0:
                if maximum-1 not in work_dict:
                    work_dict[maximum-1] = work_dict[maximum]
                else:
                    work_dict[maximum-1] += work_dict[maximum]

            n -= work_dict[maximum]
            del work_dict[maximum]

    result = 0
    for i, j in zip(work_dict.keys(), work_dict.values()):
        if i > 0:
            result += (i**2)*j

    return result


if __name__ == "__main__":
    n = 4
    works = [4,3,3]
    print(solution(n, works))