def solution(s):
    num_dic = {"zero": "0", "one": "1", 'two': "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    result = ""
    tmp = ""

    for i in s:
        if i.isalpha():
            tmp += i
        else:
            result += i
        if tmp in num_dic:
            result += num_dic[tmp]
            tmp = ""

    return result


if __name__ == "__main__":
    s = "one4seveneight"
    print(solution(s))