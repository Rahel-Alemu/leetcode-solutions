from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s, k):
        cnt = Counter(s)
        mid = ''
        half_counts = {}
        for c, f in cnt.items():
            if f % 2 == 1:
                mid = c
            half_counts[c] = f // 2

        letters = sorted(half_counts.keys())
        half_len = sum(half_counts.values())

        def comb_capped(n, r, cap):
            if r < 0 or r > n:
                return 0
            if r > n - r:
                r = n - r
            result = 1
            for i in range(r):
                result = result * (n - i) // (i + 1)
                if result > cap:
                    return cap + 1
            return result

        def perm_count(counts, cap):
            result = 1
            used = 0
            for c in counts:
                if c == 0:
                    continue
                used_new = used + c
                if result > cap:
                    return cap + 1
                factor = comb_capped(used_new, c, cap)
                if factor > cap:
                    return cap + 1
                result = result * factor
                if result > cap:
                    return cap + 1
                used = used_new
            return result

        remaining = dict(half_counts)
        total = perm_count([remaining[c] for c in letters], k)
        if total < k:
            return ""

        result_half = []
        for _ in range(half_len):
            placed = False
            for c in letters:
                if remaining[c] == 0:
                    continue
                remaining[c] -= 1
                cnts = [remaining[x] for x in letters]
                cnt_perm = perm_count(cnts, k)
                if cnt_perm >= k:
                    result_half.append(c)
                    placed = True
                    break
                else:
                    k -= cnt_perm
                    remaining[c] += 1
            if not placed:
                return ""

        half_str = ''.join(result_half)
        return half_str + mid + half_str[::-1]