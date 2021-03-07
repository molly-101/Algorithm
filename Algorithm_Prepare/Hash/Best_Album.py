def solution(genres, plays):
    play_count = {}
    song_dict = {}
    result = []

    tmp = 0
    for genre, play in zip(genres, plays):
        if genre not in play_count:
            play_count[genre] = play
            song_dict[genre] = [[play, tmp]]
        else:
            play_count[genre] += play
            song_dict[genre].append([play,tmp])
        tmp += 1

    for genre in sorted(play_count, reverse=True):
        song_count = 0
        maximum_play = 100000
        song_list = []
        for song in sorted(song_dict[genre], key= lambda x:(x[0], x[1]), reverse=True):



    return result


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres,plays))