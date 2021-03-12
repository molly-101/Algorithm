def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    state = ""
    str1_dic = {}

    if str1 == str2:
        return 65536

    for i in range(len(str1)):
        if state.isalpha() and str1[i].isalpha():
            if state + str1[i] not in str1_dic:
                str1_dic[state + str1[i]] = 1
            else:
                str1_dic[state + str1[i]] += 1

        state = str1[i]

    maximum = sum(str1_dic.values())
    minimum = 0
    state = str2[0]
    cnt = 0

    for i in range(1, len(str2)):
        if state.isalpha() and str2[i].isalpha():
            if state + str2[i] in str1_dic:
                str1_dic[state + str2[i]] -= 1
                if str1_dic[state + str2[i]] == 0:
                    del str1_dic[state + str2[i]]
                minimum += 1
                state = str2[i]
                continue
            cnt += 1

        state = str2[i]

    if maximum == 0:
        return 0
    return int(minimum / (maximum + cnt) * 65536)


if __name__ == "__main__":
    str1 = "aa1+aa2"
    str2 = "AAAA12"
    print(solution(str1, str2))