import numpy as np

class Solution(object):
    def uniqueXorTriplets(self, nums):
        maxv = max(nums)
        b = maxv.bit_length()
        N = 1 << b

        def fwht(a):
            a = a.astype(np.int64)
            length = len(a)
            h = 1
            while h < length:
                a = a.reshape(-1, 2, h)
                x = a[:, 0, :].copy()
                y = a[:, 1, :].copy()
                a[:, 0, :] = x + y
                a[:, 1, :] = x - y
                a = a.reshape(length)
                h *= 2
            return a

        f = np.zeros(N, dtype=np.int64)
        for v in nums:
            f[v] = 1

        F = fwht(f.copy())
        F2 = F * F
        cntA = fwht(F2) // N
        A = (cntA > 0).astype(np.int64)

        FA = fwht(A.copy())
        Ff = fwht(f.copy())
        prod = FA * Ff
        cntT = fwht(prod) // N

        return int(np.sum(cntT > 0))