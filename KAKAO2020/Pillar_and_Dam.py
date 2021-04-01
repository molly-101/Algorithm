def solution(n, build_frame):
    result = set()

    for x, y, a, b in build_frame:
        frame = (x, y, a)
        print(frame)
        if b == 1:
            result.add(frame)
            if is_impossible(result):
                result.remove(frame)
        else:
            result.remove(frame)
            if is_impossible(result):
                result.add(frame)
        print(result)

    return sorted(result, key=lambda x: (x[0], x[1], x[2]))


def is_impossible(result):
    pillar, dam = 0, 1
    for x, y, a in result:
        if a == 0: # pillar
            if y != 0 and (x, y, dam) not in result and (x-1, y, dam) not in result and (x, y-1, pillar) not in result:
                return True
        else: # dam
            if (x+1, y-1, pillar) not in result and (x, y-1, pillar) not in result:
                if (x-1, y, dam) not in result or (x+1, y, dam) not in result:
                    return True

    return False


if __name__ == "__main__":
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    print(solution(n, build_frame))