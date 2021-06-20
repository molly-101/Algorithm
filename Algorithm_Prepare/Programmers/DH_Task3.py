# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    memo = {}
    result = 1
    lt = 0

    for i in range(len(A)):
        if A[i] not in memo:
            memo[A[i]] = 1
        else:
            memo[A[i]] += 1

        while len(memo) > 2:
            if memo[A[lt]] == 1:
                del memo[A[lt]]
            else:
                memo[A[lt]] -= 1

            lt += 1

        result = max(result, i - lt + 1)

    return result


if __name__ == "__main__":
    A = [2,3,4,1,3,4,3,2,1,2,3,2,3,2,3,2]
    print(solution(A))