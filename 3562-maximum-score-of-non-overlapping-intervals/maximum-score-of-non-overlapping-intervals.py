import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)
        indexed = sorted((interval[0], interval[1], interval[2], i) for i, interval in enumerate(intervals))
        lefts = [x[0] for x in indexed]

        # dp[i][quota] = (weight, selected_tuple) for intervals[i:], with `quota` picks allowed
        dp = [[(0, ())] * 5 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, weight, orig_idx = indexed[i]
            j = bisect.bisect_right(lefts, r)
            row = dp[i]
            next_row = dp[i + 1]
            row_j = dp[j]
            for quota in range(5):
                skip = next_row[quota]
                if quota == 0:
                    row[quota] = skip
                    continue
                nres_w, nres_sel = row_j[quota - 1]
                pick_sel = tuple(sorted(nres_sel + (orig_idx,)))
                pick_w = weight + nres_w
                if pick_w > skip[0] or (pick_w == skip[0] and pick_sel < skip[1]):
                    row[quota] = (pick_w, pick_sel)
                else:
                    row[quota] = skip

        return list(dp[0][4][1])