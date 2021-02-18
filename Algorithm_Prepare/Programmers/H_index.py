def solution(citations):
    maximum, minimum = max(citations), min(citations)
    for h in range(maximum, minimum, -1):
        cnt = 0
        for citation in citations:
            if citation >= h:
                cnt += 1
        if cnt >= h:
            return h
    else:
        return 0


if __name__ == "__main__":
    citations = [7,7,7,7,5]
    print(solution(citations))