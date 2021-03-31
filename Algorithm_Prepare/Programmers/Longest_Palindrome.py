def solution(s):

    for i in range(len(s), 1, -1):
        for j in range(0, len(s)+1-i):
            for k in range(i//2):
                if s[j:j+i][k] != s[j:j+i][-k-1]:
                    break
            else:
                return i
    return 1


if __name__ == "__main__":
    s = "abcdcba"
    print(solution(s))