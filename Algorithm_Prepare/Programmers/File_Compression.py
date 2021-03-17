def solution(msg):
    dic = {}
    result = []

    for i in range(1,27):
        dic[chr(i+64)] = i

    num = 27
    i = 0
    q = 0

    while i < len(msg) and q == 0:
        tmp = 0

        for j in range(i, len(msg)):
            if msg[i:j+1] in dic:
                tmp = dic[msg[i:j+1]]
                if j == len(msg)-1:
                    q = 1
            else:
                dic[msg[i:j+1]] = num
                num += 1
                break

        result.append(tmp)
        i = j

    return result


if __name__ == "__main__":
    msg = "KAKAO"
    print(solution(msg))