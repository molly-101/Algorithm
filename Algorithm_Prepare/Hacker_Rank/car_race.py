def solution(obstacleLanes):
    now = 2
    i = 0
    result = 0

    while i < len(obstacleLanes):

        if obstacleLanes[i] == now:
            i += 1
            for j in range(i, len(obstacleLanes)):
                if obstacleLanes[j] != now:
                    i = j
                    now = 6 - now - obstacleLanes[j]
                    result += 1
                    break
            else:
                result += 1
                break
        else:
            i += 1

    return result


if __name__ == "__main__":
    print(solution([2,1,3,3,3,3,3]))