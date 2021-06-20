# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    datas = ["rar", "zip", "tgz"]
    result = 0
    query = S.split()

    for i in range(len(query) // 3):
        date = query[3 * i]
        size = query[3 * i + 1].zfill(6)
        data = query[3 * i + 2]

        if size >= "245760":
            continue
        if data[-3:].lower() not in datas:
            continue
        if date >= "1995-10-13":
            continue

        result += 1

    if result > 0:
        return str(result)
    else:
        return "NO FILES"


if __name__ == "__main__":
    S = "1988-08-29        956 system.zip 1976-09-16     126976 old-photos.tgz 1987-02-03     118784 logs.rar 1961-12-04  703594496 very-long-filename.rar 1980-08-03          2 DELETE-THIS.TXT 2014-08-23        138 important.rar 2001-08-26     595968 MOONLIGHT-SONATA.FLAC 1967-11-30     245760 archive.rar 1995-10-13        731 file.tgz"
    print(solution(S))