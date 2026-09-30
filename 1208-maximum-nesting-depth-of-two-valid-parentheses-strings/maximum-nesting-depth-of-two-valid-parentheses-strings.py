class Solution(object):
    def maxDepthAfterSplit(self, seq):
        result = []
        depth = 0
        for ch in seq:
            if ch == '(':
                depth += 1
                result.append(depth % 2)
            else:
                result.append(depth % 2)
                depth -= 1
        return result