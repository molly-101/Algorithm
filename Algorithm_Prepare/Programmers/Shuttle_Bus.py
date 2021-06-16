from collections import deque


def solution(n, t, m, timetable):
    timetable = sorted(timetable)
    int_timetable = deque()
    start = 540
    stack = []

    # make integer timetable
    for i in timetable:
        int_timetable.append(int(i[:2]) * 60 + int(i[3:]))

    now, cnt = 0, 0

    for i in range(n):
        now = start + t * i
        cnt = m

        while int_timetable and cnt > 0:
            if int_timetable[0] <= now:
                cnt -= 1
                stack.append(int_timetable.popleft())
            else:
                break

    if cnt > 0:
        return makeStringTime(now)
    else:
        tmp = stack.pop()
        return makeStringTime(tmp - 1)


def makeStringTime(time):
    hour = str(time // 60).zfill(2)
    minute = str(time - (time // 60) * 60).zfill(2)
    return hour + ":" + minute