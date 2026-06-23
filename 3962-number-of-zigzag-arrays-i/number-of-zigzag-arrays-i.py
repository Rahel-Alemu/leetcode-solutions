class Solution(object):
    def zigZagArrays(self, n, l, r):
        m = r - l + 1
        MOD = 10**9 + 7
        
        UP = list(range(m))
        
        for _ in range(3, n + 1):
            new_UP = [0] * m
            s = 0
            for i in range(1, m):
                s = (s + UP[m - i]) % MOD
                new_UP[i] = s
            UP = new_UP
            
        return (sum(UP) * 2) % MOD