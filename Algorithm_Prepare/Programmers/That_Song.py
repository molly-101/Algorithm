def solution(m, musicinfos):
    # 1. 재생된 시간 계산
    result = []
    stack_m = []
    for i in range(len(m)):
        if not stack_m:
            stack_m.append(m[i])
        else:
            if m[i] == "#":
                stack_m.append(stack_m.pop() + "#")
            else:
                stack_m.append(m[i])

    for musicinfo in musicinfos:
        start, end, name, code = musicinfo.split(",")
        playtime = (int(end[:2]) - int(start[:2])) * 60 + int(end[3:]) - int(start[3:])
        stack = []

        for i in code:
            if i == "#":
                stack.append(stack.pop() + "#")
            else:
                stack.append(i)
        played = []

        if len(stack_m) > playtime:
            continue
        else:
            for _ in range(playtime // len(stack)):
                played += stack
            played += stack[:playtime % len(stack)]

            for i in range(len(played) - len(stack_m) + 1):
                for j in range(len(stack_m)):
                    if played[i + j] != stack_m[j]:
                        break
                else:
                    if not result:
                        result = [playtime, name]
                    else:
                        if result[0] < playtime:
                            result = [playtime, name]

                    break
    if not result:
        return "(None)"
    else:
        return result[1]


if __name__ == "__main__":
    m = "ABC#"
    musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    print(solution(m, musicinfos))