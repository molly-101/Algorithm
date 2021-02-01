def solution(new_id):
    if correct_id(new_id):
        print(new_id)
        return new_id
    else:
        result = partSeven(partSix(partFive(partFour(partThree(partTwo(partOne(new_id)))))))
        return result


def partOne(new_id): # 1단계: new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    saveOrd = []
    for i in range(len(new_id)):
        if 65 <= ord(new_id[i]) <= 90:
            saveOrd.append(ord(new_id[i])+32)
        else:
            saveOrd.append(ord(new_id[i]))
    return "".join(chr(i) for i in saveOrd)


def partTwo(new_id): # 2단계: new_id에서 알파벳 소문자, 숫자, -, _, . 을 제외한 모든 문자를 제거
    tmp = ""
    for i in range(len(new_id)):
        if 48 <= ord(new_id[i]) <= 57 or 97 <= ord(new_id[i]) <= 122 or ord(new_id[i]) == 46 or ord(new_id[i]) == 45 or ord(new_id[i]) == 95:
            tmp += new_id[i]
    return tmp


def partThree(new_id): # 3단계: new_id 에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    dotCnt = 0
    tmp = ""
    for i in new_id:
        if i == ".":
            if dotCnt == 0:
                dotCnt += 1
                tmp += i
        else:
            dotCnt = 0
            tmp += i
    return tmp

def partFour(new_id): # 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if new_id == "":
        return new_id
    while new_id[0] == "." or new_id[len(new_id)-1] == "." and new_id != "":
        if new_id[0] == ".":
            new_id = new_id[1:]
            if new_id == "":
                break
        if new_id[len(new_id)-1] == ".":
            new_id = new_id[:len(new_id)-1]
    return new_id


def partFive(new_id): #new_id가 빈 문자열이라면, new_id 에 "a"를 대입합니다.
    if new_id == "":
        new_id += "a"
    return new_id


def partSix(new_id): # 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(new_id)>=16:
        new_id = new_id[:15]
        if new_id[len(new_id)-1] == ".":
            new_id = new_id[:14]
        return new_id
    else:
        return new_id


def partSeven(new_id): # new_id의 길이가 2자 이하라면, New_id의 마지막 문자를 new_id의 길이가 3이 될때까지 반복해서 끝에 붙입니다.
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[len(new_id)-1]
    return new_id


def correct_id(id): #옳은 문자열인지 판단하는 함수입니다.
    if 3>len(id) or 15<len(id):
        return False
    else:
        dotCnt = 0
        for i in range(len(id)):
            if i == 0 or i == len(id)-1:
                if id[i] == ".":
                    return False

            if 97<= ord(id[i]) <= 122 or ord(id[i]) == 46 or ord(id[i]) == 45 or ord(id[i]) == 95:
                if id[i] == ".":
                    dotCnt += 1
                else:
                    dotCnt = 0
            else:
                return False
            if dotCnt == 2:
                return False
        else:
            return True


if __name__ == "__main__":
    new_ids = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
    for new_id in new_ids:
        print(solution(new_id))
