class Solution(object):
    def numberOfSpecialChars(self, word):
        chars = set(word)
        return sum(1 for c in "abcdefghijklmnopqrstuvwxyz" if c in chars and c.upper() in chars)