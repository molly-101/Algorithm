def solution(s):
    # 1. make split s
    spl = s[2:-2].split("},{")
    res = [i.split(",") for i in spl]

    # 2. sorting res
    res.sort(key=lambda x: len(x))

    # 3. result
    result = []
    hashMap = {}
    for i in res:
        for j in i:
            if j not in hashMap:
                hashMap[j] = True
                result.append(int(j))
                break

    return result


if __name__ == "__main__":
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))