class Solution(object):
    def reverseDegree(self, s):
        total = 0
        for i, ch in enumerate(s):
            reversed_index = 26 - (ord(ch) - ord('a'))
            total += reversed_index * (i + 1)
        return total