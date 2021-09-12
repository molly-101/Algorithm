def paperCuttings(textLength, starting, ending):
    dic = {}
    arr = []
    result = 0
    for i, j in zip(starting, ending):
        if i in dic:
            if j not in dic[i]:
                dic[i][j] = True
        else:
            dic[i] = {j: True}

    for i in dic.keys():
        for j in dic[i].keys():
            arr.append([i, j])

    arr = sorted(arr, key=lambda x: (x[0], x[1]))
    for i in range(len(arr)):
        end = arr[i][1]
        lt = i
        rt = len(arr) - 1
        while lt <= rt:
            mid = (lt + rt) // 2
            if arr[mid][0] > end:
                rt = mid - 1
            else:
                lt = mid + 1
        if rt != lt:
            result += len(arr) - rt - 1
    return result