def solution(record):
    logs = []  # save Enter, Leave
    result = []
    usr = {}
    for i in record:
        data = i.split()
        if data[0] == "Enter":
            usr[data[1]] = data[2]
        if data[0] == "Change":
            usr[data[1]] = data[2]
            continue
        logs.append([data[0], data[1]])

    for log in logs:
        if log[0] == "Enter":
            result.append(usr[log[1]] + "님이 들어왔습니다.")
        else:
            result.append(usr[log[1]] + "님이 나갔습니다.")

    return result


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    solution(record)