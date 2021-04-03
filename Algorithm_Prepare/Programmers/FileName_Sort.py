def solution(files):
    answer, result = [], []

    for file in files:
        head, number, tail = "", "", ""
        state = "h"
        for i in file:
            if state == "h" and not i.isdigit():
                head += i
            elif state == "h" and i.isdigit():
                number += i
                state = "n"
            elif state == "n" and i.isdigit():
                number += i
            elif state == "n" and not i.isdigit():
                tail += i
                state = "t"
            elif state == "t":
                tail += i

        answer.append([head, number, tail])

    answer = sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))

    for i in answer:
        result.append("".join(i))

    return result


if __name__ == "__main__":
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

    a = ["MUZI", "muzi", "Muzi"]
    print(int("0021"))
    print(sorted(a, key=lambda x:x.lower()))
    print(solution(files))