def solution(numbers):
    result = []

    for number in numbers:
        bin_num = "0" + bin(number)[2:]
        num = 1

        for i in range(1, len(bin_num)+1):
            if bin_num[-i] == "0":
                if i <= 2:
                    result.append(number + num)
                else:
                    for j in range(i - 2):
                        num += 2 ** j
                    result.append(number + num)
                break

    return result


def bestSolution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val + 1)) >> 2) + val + 1)

    return answer



if __name__ == "__main__":
    numbers = [2,7,11]
    print(solution(numbers))