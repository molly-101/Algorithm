def solution(array):
    stack = []
    result = [-1]*len(array)

    for i in range(len(array)):
        if not stack:
            stack.append([array[i], i])
        else:
            while stack:
                if stack[-1][0] < array[i]:
                    tmp = stack.pop()
                    if result[tmp[1]] == -1 or tmp[1] - result[tmp[1]] > i - tmp[1]:
                        result[tmp[1]] = i
                elif stack[-1][0] > array[i]:
                    result[i] = stack[-1][1]
                    break
                else:
                    result[i] = result[stack[-1][1]]
                    break
            stack.append([array[i], i])

    return result


if __name__ == "__main__":
    array = [7,4,4,2,9,4,6,0]
    print(solution(array))