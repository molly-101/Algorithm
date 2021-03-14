def solution(s):
    s = s.lower()
    res = s.split()
    result = ""

    for i in res:
        li = list(i)
        if li[0].isalpha():
            li[0] = li[0].upper()

        result += "".join(li)
        result += " "

    return result[:-1]


if __name__ == '__main__':
    s = "3people unFollowed   me"
    print(solution(s))