import math


def euclidean_similarity(u1, u2):
    return math.sqrt(sum(pow(u1[i]-u2[i],2) for i in range(len(u1))))


def cosine_similarity(u1,u2):
    return sum(u1[i]*u2[i] for i in range(len(u1)))


def make_normalize(res):
    normalized_data = []
    for item in res:
        tmp = []
        den = math.sqrt(sum(pow(value,2) for value in item))
        for value in item:
            tmp.append(value/den)
        normalized_data.append(tmp)
    return normalized_data


if __name__ == "__main__":
    # used euclidean similarity value
    user1 = [5, 1, 1, 4]
    user2 = [4, 1, 2, 3]
    user3 = [1, 2, 4, 1]

    # used cosine base similarity value
    item1 = [3,2,1]
    item2 = [4,2,3]
    item3 = [2,4,5]
    data = [item1,item2,item3]
    normalized_data = make_normalize(data)
    print(normalized_data)
    print(cosine_similarity(normalized_data[0],normalized_data[2]))