def solution(food_times, k):
    # save memo in food counts
    food_memo = {}
    for i in food_times:
        if i not in food_memo:
            food_memo[i] = 1
        else:
            food_memo[i] += 1

    res = sorted(food_memo)
    foods = len(food_times)  # food 개수
    now = 0  # save

    for i in res:
        if (i - now) * foods <= k:
            k -= (i - now) * foods
            foods -= food_memo[i]
            del food_memo[i]
            now = i
        else:
            k -= (k // foods) * foods
            break
    else:
        return -1

    for i in range(len(food_times)):
        if food_times[i] > now:
            k -= 1
            if k == -1:
                return i + 1