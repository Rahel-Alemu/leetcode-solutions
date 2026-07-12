class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_unique = sorted(list(set(arr)))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        return [rank_map[x] for x in arr]