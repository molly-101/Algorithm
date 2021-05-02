def solution(inputString):
    stack = []
    cnt = 0
    for i in range(len(inputString)):
        if not stack:
            if inputString[i] == ">" or inputString[i] == "}" or inputString[i] == ")" or inputString[i] == "]":
                return i*(-1)
            if inputString[i] == "<" or inputString[i] == "{" or inputString[i] == "(" or inputString[i] == "[":
                stack.append([inputString[i],i])
        else:
            if inputString[i] == "<" or inputString[i] == "{" or inputString[i] == "(" or inputString[i] == "[":
                stack.append([inputString[i],i])
                continue
            if inputString[i] == ">" or inputString[i] == "}" or inputString[i] == "]" or inputString[i] == ")":
                if stack[-1][0] == "<" and inputString[i] == ">":
                    stack.pop()
                    cnt += 1
                elif stack[-1][0] == "{" and inputString[i] == "}":
                    stack.pop()
                    cnt += 1
                elif stack[-1][0] == "[" and inputString[i] == "]":
                    stack.pop()
                    cnt += 1
                elif stack[-1][0] == "(" and inputString[i] == ")":
                    stack.pop()
                    cnt += 1
                else:
                    return i*(-1)

    if stack:
        return -1*(len(inputString)-1)
    else:
        return cnt


if __name__ == "__main__":
    inputString = "line [({<plus>)}]"
    print(solution(inputString))
