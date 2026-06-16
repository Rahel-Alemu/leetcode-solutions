class Solution(object):
    def processStr(self, s):
        res = []
        for c in s:
            if c == '*':
                if res:
                    res.pop()
            elif c == '#':
                res.extend(res)
            elif c == '%':
                res.reverse()
            else:
                res.append(c)
        return "".join(res)