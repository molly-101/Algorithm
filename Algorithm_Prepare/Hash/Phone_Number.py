def solution(phone_book):
    phone_book_dict = {}

    for i in phone_book:
        tmp = phone_book_dict
        for j in i:
            if j not in tmp:
                tmp[j] = {}
                tmp = tmp[j]
            else:
                tmp = tmp[j]
        tmp["*"] = 1

    for i in phone_book:
        tmp = phone_book_dict
        star_count = 0

        for j in i:
            if "*" not in tmp[j].keys():
                tmp = tmp[j]
                continue
            else:
                tmp = tmp[j]
                star_count += 1

        if star_count > 1:
            return False

    else:
        return True


if __name__ == "__main__":
    phone_book = ["12","123","1235","567","88"]
    print(solution(phone_book))