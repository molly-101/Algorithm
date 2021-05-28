def solution(play_time, adv_time, logs):
    res = [0] * 360000
    ad_time = time_sec(adv_time)
    pl_time = time_sec(play_time)

    # res에 시작부분에는 +1 끝나는 부분에는 -1을
    for log in logs:
        time_s, time_e = time_sec(log[:8]), time_sec(log[9:])
        res[time_s] += 1
        res[time_e] -= 1

    # 첫 번째 루프에는 i 시간에 보고있는 시청자 수
    # 두 번째 루프에는 i 시간에 보고있는 누적 시청자 수
    for _ in range(2):
        for i in range(1, pl_time):
            res[i] += res[i - 1]

    result = [0, 0]

    # 누적시청자 최대 시간 판별법: i시간대 누적시청자 - i-ad_time 시간대 누적시청자가 최대일 때
    for i in range(ad_time - 1, pl_time):
        if result[0] < res[i] - res[i - ad_time]:
            result = [res[i] - res[i - ad_time], i - ad_time + 1]

    return time_string(result[1])


# string 시:분:초 시간 -> int 초단위 시간
def time_sec(time):
    return int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:8])


# int 초단위 시간 -> string 시:분:초 시간으로 변경
def time_string(time):
    hour = time // 3600
    min = (time - hour * 3600) // 60
    sec = (time - hour * 3600 - min * 60)
    return str(hour).rjust(2, '0') + ":" + str(min).rjust(2, "0") + ":" + str(sec).rjust(2, "0")



if __name__ == "__main__":
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs =  ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    print(solution(play_time, adv_time, logs))