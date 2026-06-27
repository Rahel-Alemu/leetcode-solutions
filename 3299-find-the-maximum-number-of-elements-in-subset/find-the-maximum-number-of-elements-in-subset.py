class Solution(object):
    def maximumLength(self, nums):
        from collections import Counter
        
        counts = Counter(nums)
        max_len = 1
        
        if 1 in counts:
            c = counts[1]
            if c % 2 == 0:
                max_len = max(max_len, c - 1)
            else:
                max_len = max(max_len, c)
                
        for x in counts:
            if x == 1:
                continue
            
            curr = x
            length = 0
            while counts.get(curr, 0) >= 2:
                length += 2
                curr = curr * curr
                
            if counts.get(curr, 0) >= 1:
                length += 1
            else:
                length -= 1
                
            if length > max_len:
                max_len = length
                
        return max_len