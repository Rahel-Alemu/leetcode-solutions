class Solution(object):
    def numberOfSubstrings(self, s):
        last = [-1, -1, -1]
        res = 0
        for i, c in enumerate(s):
            last[ord(c) - 97] = i
            res += min(last) + 1
        return res