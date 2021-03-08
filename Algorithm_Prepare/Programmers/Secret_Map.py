def solution(n, arr1, arr2):
    result = []

    for a1, a2 in zip(arr1, arr2):
        build = ""
        for i, j in zip(trans_binary(a1, n), trans_binary(a2, n)):
            if i == "0" and j == "0":
                build += " "
            else:
                build += "#"

        result.append(build)

    return result


def trans_binary(num, n):
    print(list(bin(num)[2:]))
    b_num = list(bin(num)[2:])
    res = ["0"] * (n - len(b_num)) + b_num

    return res


if __name__ == "__main__":
    n = 6
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]

    print(solution(n,arr1,arr2))