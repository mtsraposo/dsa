from bisect import bisect, bisect_left
from itertools import groupby


def rank_high_scores(player, ranked):
    high_ranks = []
    if len(player):
        index = bisect_left(player, ranked[-1])
        print(player, index)
        if index < len(player):
            high_scores = player[index:]
            high_ranks = [1] * len(high_scores)
            player = player[:index]
    return player, high_ranks


def rank_low_scores(player, ranked, ranked_count):
    # Start with scores that are below the lowest rank
    low_ranks = []
    if len(player):
        index = bisect_left(player, ranked[0])
        print(player, index)
        if index > 0:
            low_scores = player[:index]
            low_ranks += [ranked_count + 1] * len(low_scores)
            player = player[index:]
    return player, low_ranks


def rank_middle_scores(player, ranked):
    # For the remaining scores, find where they would be inserted in the list
    # and repeat for the remainder of the list
    middle_ranks = []
    if len(player):
        index_max_player = bisect(ranked, player[-1])
        index_min_player = bisect(ranked, player[0])
        print(player, index_min_player, index_max_player)
        for p, g in groupby(player):
            index = bisect(ranked, p, lo=index_min_player, hi=index_max_player)
            middle_ranks += [len(ranked) - index + 1] * len(list(g))
            index_min_player = index
    return middle_ranks


def climbingLeaderboard(ranked, player):
    # Get unique ordered ranks
    ranked = list(dict.fromkeys(ranked).keys())
    ranked_count = len(ranked)
    ranked.reverse()

    player, high_ranks = rank_high_scores(player, ranked)
    player, low_ranks = rank_low_scores(player, ranked, ranked_count)
    middle_ranks = rank_middle_scores(player, ranked)

    return low_ranks + middle_ranks + high_ranks


if __name__ == '__main__':
    s = """7
    100 100 50 40 40 20 10
    4
    5 25 50 120"""
    s = s.split('\n')
    ranked_count = int(s[0])
    ranked = list(map(int, s[1].rstrip().split()))
    player_count = int(s[2].strip())
    player = list(map(int, s[3].rstrip().split()))

    print(climbingLeaderboard(ranked, player))
