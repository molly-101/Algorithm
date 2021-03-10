def solution(s):
    res = returnList(s)
    result = []
    res_dict = {}
    save_sum = 0

    for i in res:
        tmp = sum(i)
        result.append(tmp-save_sum)
        save_sum = tmp
    return result


def returnList(s):
    res, tmp = [], []
    a = ""
    l, r = 0, 0
    for i in s[1:-1]:
        if i == "{":
            l += 1
            continue
        if i == "}":
            tmp.append(int(a))
            a = ""
            r += 1
            res.append(tmp)
            tmp = []
        if l != r:
            if i.isdigit():
                a += i
            if i == ",":
                tmp.append(int(a))
                a = ""
    return sorted(res, key=lambda x: len(x))



if __name__ == "__main__":
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    solution(s)