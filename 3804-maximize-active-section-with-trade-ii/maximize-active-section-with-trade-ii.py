import math

class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        rc, rs, rl = [], [], []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            rc.append(s[i]); rs.append(i); rl.append(j - i)
            i = j
        k = len(rc)
        re = [rs[t] + rl[t] - 1 for t in range(k)]
        total = sum(l for c, l in zip(rc, rl) if c == '1')
        pos2run = [0] * n
        for t in range(k):
            for p in range(rs[t], re[t] + 1):
                pos2run[p] = t

        NEG = float('-inf')
        INF = float('inf')

        def build(arr, f):
            if k == 0:
                return []
            table = [arr[:]]
            j = 1
            while (1 << j) <= k:
                prev = table[-1]
                half = 1 << (j - 1)
                cur = [f(prev[x], prev[x + half]) if x + half < k else prev[x] for x in range(k - (1 << j) + 1)]
                table.append(cur)
                j += 1
            return table

        def query(table, l, r, f, default):
            if l > r:
                return default
            length = r - l + 1
            j = length.bit_length() - 1
            half = 1 << j
            return f(table[j][l], table[j][r - half + 1])

        oneLen = [rl[t] if rc[t] == '1' else INF for t in range(k)]
        zeroLen = [rl[t] if rc[t] == '0' else NEG for t in range(k)]
        A = [rl[t-1] + rl[t+1] if 0 < t < k - 1 and rc[t] == '1' else NEG for t in range(k)]

        minT = build(oneLen, min)
        maxZ = build(zeroLen, max)
        maxA = build(A, max)

        ans = []
        for l, r in queries:
            segL = pos2run[l]
            segR = pos2run[r]
            if segL == segR:
                ans.append(total)
                continue
            aL = re[segL] - l + 1
            aR = r - rs[segR] + 1
            cL, cR = rc[segL], rc[segR]

            min1 = query(minT, segL + 1, segR - 1, min, INF)
            maxZero = NEG
            if cL == '0':
                maxZero = max(maxZero, aL)
            if cR == '0':
                maxZero = max(maxZero, aR)
            maxZero = max(maxZero, query(maxZ, segL + 1, segR - 1, max, NEG))

            term2 = maxZero - min1 if min1 < INF and maxZero > NEG else NEG

            term1 = NEG
            if segL + 1 <= segR - 1 and rc[segL + 1] == '1':
                left = aL
                right = aR if segL + 2 == segR else rl[segL + 2]
                term1 = max(term1, left + right)
            if segL + 1 <= segR - 1 and rc[segR - 1] == '1':
                right = aR
                left = aL if segR - 2 == segL else rl[segR - 2]
                term1 = max(term1, left + right)
            term1 = max(term1, query(maxA, segL + 2, segR - 2, max, NEG))

            gain = max(0, term1, term2)
            ans.append(total + gain)

        return ans