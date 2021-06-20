# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    result = []
    memo = {}
    names = S.split(";")
    for n in names:
        tmp = n.split(" ")
        if tmp[0] == '':
            first = tmp[1].lower()
        else:
            first = tmp[0].lower()

        last = tmp[-1].lower()

        name = del_hyphen(last) + "_" + del_hyphen(first)

        if name not in memo:
            memo[name] = 1
        else:
            memo[name] += 1
            name += str(memo[name])

        result.append(n + " <" + name + "@" + C.lower() + ".com" + ">")

    return ";".join(result)


def del_hyphen(word):
    result = ""
    for i in word:
        if i.isalpha():
            result += i
    return result


if __name__ == "__main__":
    S = "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
    C = "Example"
    print(solution(S, C))