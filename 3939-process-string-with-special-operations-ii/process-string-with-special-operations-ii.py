class Solution(object):
    def processStr(self, s, k):
        n = len(s)
        L = [0] * n
        curr = 0
        for i in range(n):
            c = s[i]
            if c == '*':
                curr = curr - 1 if curr > 0 else 0
            elif c == '#':
                curr *= 2
            elif c == '%':
                pass
            else:
                curr += 1
            L[i] = curr
            
        if k < 0 or k >= L[-1]:
            return '.'
            
        K = k
        for i in range(n - 1, -1, -1):
            c = s[i]
            prev_L = L[i-1] if i > 0 else 0
            
            if c == '*':
                pass
            elif c == '#':
                if K >= prev_L:
                    K -= prev_L
            elif c == '%':
                K = prev_L - 1 - K
            else:
                if K == prev_L:
                    return c
                    
        return '.'