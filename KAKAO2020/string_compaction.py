def solution(s):
    minimum = len(s)
    for i in range(1, len(s)//2+1):
        start, startcnt = "", 0
        length = len(s)
        for j in range(0,length//i):
            alpha = s[j*i:j*i+i]
            if start == "":
                start = alpha
                startcnt += 1
            else:
                if start == alpha:
                    startcnt += 1
                else:
                    start = alpha
                    if startcnt > 1:
                        length = length - (startcnt-1)*i + len(str(startcnt))
                    startcnt = 1
        if startcnt > 1:
            length = length - (startcnt - 1) * i + len(str(startcnt))
        if length < minimum:
            minimum = length
    return minimum


if __name__ == "__main__":
    res = ["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]

    for i in res:
        print(solution(i))