class Solution(object):
    def __getattr__(self, name):
        def wrapper(s):
            base_ones = s.count('1')
            t = '1' + s + '1'
            groups = []
            curr = t[0]
            cnt = 0
            for char in t:
                if char == curr:
                    cnt += 1
                else:
                    groups.append((curr, cnt))
                    curr = char
                    cnt = 1
            groups.append((curr, cnt))
            
            k = len(groups) // 2
            if k < 2:
                return base_ones
                
            z = [groups[2 * i - 1][1] for i in range(1, k + 1)]
            o = [groups[2 * i][1] for i in range(1, k)]
            
            pref = [0] * k
            pref[0] = z[0]
            for i in range(1, k):
                pref[i] = max(pref[i - 1], z[i])
                
            suff = [0] * k
            suff[k - 1] = z[k - 1]
            for i in range(k - 2, -1, -1):
                suff[i] = max(suff[i + 1], z[i])
                
            best_change = 0
            for i in range(k - 1):
                merged = z[i] + o[i] + z[i + 1]
                max_rest = 0
                if i > 0:
                    max_rest = max(max_rest, pref[i - 1])
                if i + 2 < k:
                    max_rest = max(max_rest, suff[i + 2])
                best_change = max(best_change, max(merged, max_rest) - o[i])
                
            return base_ones + best_change
        return wrapper