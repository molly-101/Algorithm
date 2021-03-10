def solution(n):
    number_list = [i for i in range(0, n+1)]
    l, r = 0,0
    result = 0

    while l != n or r != n:
        if sum(number_list[l:r+1]) < n:
            r += 1
        elif sum(number_list[l:r+1]) > n:
            l += 1
        else:
            result += 1
            r += 1

    return result+1


if __name__ == "__main__":
    n = 15
    solution(n)