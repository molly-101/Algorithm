def climbingLeaderboard(ranked, player):
    result = []
    for player_rate in player:
        rank_tmp = 1
        rate_tmp = ranked[0]
        for i in range(len(ranked)):
            if ranked[i] == rate_tmp: # 현재 점수와 이전 점수가 같을 경우 : 랭크 동일
                if player_rate >= ranked[i]:
                    result.append(rank_tmp)
                    ranked.insert(i,player_rate)
                    break
            else: # 현재 점수와 이전 점수가 다를 경우: 랭크 하락
                rank_tmp += 1
                rate_tmp = ranked[i]
                if player_rate >= ranked[i]:
                    result.append(rank_tmp)
                    ranked.insert(i, player_rate)
                    break
        else:
            rank_tmp += 1
            result.append(rank_tmp)
            ranked.append(player_rate)
    return result


if __name__ == "__main__":
    ranked = [100,90,90,80,75,60]
    player = [50,65,77,90,102]
    climbingLeaderboard(ranked,player)