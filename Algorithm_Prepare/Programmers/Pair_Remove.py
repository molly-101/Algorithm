def solution(s):
    s = list(s)
    while s:
        del_count = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                del s[i]
                del s[i]
                del_count += 1
                break

        if del_count == 0:
            return 0

    return 1

if __name__ == "__main__":
    s = "baabaa"
    solution(s)