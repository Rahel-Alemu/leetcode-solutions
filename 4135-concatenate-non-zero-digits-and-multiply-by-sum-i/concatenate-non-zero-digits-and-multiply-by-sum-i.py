class Solution(object):
    def __getattr__(self, name):
        return self.solve

    def solve(self, n):
        s = str(n).replace('0', '')
        if not s:
            return 0
        return int(s) * sum(int(c) for c in s)