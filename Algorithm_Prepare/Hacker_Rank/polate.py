def interpolate(n, instances, price):
    # Write your code here
    result = 0
    # 범위 내에 가격이 있을 경우에
    for i in range(len(instances)):
        # 같을 경우 price return
        if instances[i] == n:
            result = price[i]
        # want point
        elif instances[i] > n and price[i] > 0:
            for j in range(i - 1, -1, -1):
                if price[j] > 0:  # 선형추정 make 기울기
                    result = (price[i] - price[j]) / (instances[i] - instances[j]) * (n - instances[j]) + price[j]
                    break
            else:
                for j in range(i+1, len(instances)):
                    if price[j] > 0:
                        result = (price[j] - price[i]) / (instances[j] - instances[i]) * (n - instances[i]) + price[i]
                else:
                    result = price[i]
            break
    # 범위 내에 없을 경우
    else:
        for i in range(len(instances) - 1, -1, -1):
            if price[i] > 0:
                for j in range(i - 1, -1, -1):
                    if price[j] > 0:
                        result = (price[i] - price[j]) / (instances[i] - instances[j]) * (n - instances[j]) + price[j]
                        break
                else:
                    result = price[i]
                break

    return str(format(result, ".2f"))


if __name__ == "__main__":
    n = 1999
    instances = [10,25,50,100,500]
    price = [27.32, 23.13, 21.25, 18.00, 15.50]
    print(interpolate(n, instances, price))