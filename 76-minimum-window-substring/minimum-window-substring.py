from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        
        target_counts = Counter(t)
        window_counts = {}
        
        have, need = 0, len(target_counts)
        res, res_len = [-1, -1], float("inf")
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""