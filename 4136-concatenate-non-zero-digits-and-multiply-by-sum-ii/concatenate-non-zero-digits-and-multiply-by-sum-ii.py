class Solution(object):
    def __getattr__(self, name):
        return self.solve
        
    def solve(self, s, queries):
        MOD = 10**9 + 7
        m = len(s)
        
        non_zeros = []
        cnt = [0] * (m + 1)
        for i, char in enumerate(s):
            if char != '0':
                non_zeros.append(int(char))
            cnt[i+1] = len(non_zeros)
            
        K = len(non_zeros)
        pref_val = [0] * (K + 1)
        pref_sum = [0] * (K + 1)
        power10 = [1] * (K + 1)
        
        for i in range(K):
            val = non_zeros[i]
            pref_val[i+1] = (pref_val[i] * 10 + val) % MOD
            pref_sum[i+1] = pref_sum[i] + val
            power10[i+1] = (power10[i] * 10) % MOD
            
        ans = []
        for l, r in queries:
            L = cnt[l]
            R = cnt[r+1] - 1
            if L > R:
                ans.append(0)
            else:
                length = R - L + 1
                x = (pref_val[R+1] - pref_val[L] * power10[length]) % MOD
                s_sum = pref_sum[R+1] - pref_sum[L]
                ans.append((x * s_sum) % MOD)
                
        return ans