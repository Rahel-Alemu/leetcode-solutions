class Solution(object):
    def __getattr__(self, name):
        return self.solve

    def solve(self, words, weights):
        res = []
        for word in words:
            w = sum(weights[ord(c) - 97] for c in word)
            res.append(chr(122 - (w % 26)))
        return "".join(res)