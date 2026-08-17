import numpy as np

class Solution(object):
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix = np.zeros(n + 1, dtype=np.int64)
        prefix[1:] = np.cumsum(stoneValue)
        dp = np.zeros((n, n), dtype=np.int64)

        for length in range(2, n + 1):
            num_i = n - length + 1
            i_arr = np.arange(num_i).reshape(-1, 1)
            t_arr = np.arange(length - 1).reshape(1, -1)
            k = i_arr + t_arr
            j_arr = i_arr + (length - 1)

            leftSum = prefix[k + 1] - prefix[i_arr]
            rightSum = prefix[j_arr + 1] - prefix[k + 1]
            dpi = dp[i_arr, k]
            dpk1j = dp[k + 1, j_arr]

            cand = np.where(
                leftSum < rightSum, leftSum + dpi,
                np.where(leftSum > rightSum, rightSum + dpk1j,
                          leftSum + np.maximum(dpi, dpk1j))
            )
            dp[i_arr[:, 0], j_arr[:, 0]] = cand.max(axis=1)

        return int(dp[0, n - 1])