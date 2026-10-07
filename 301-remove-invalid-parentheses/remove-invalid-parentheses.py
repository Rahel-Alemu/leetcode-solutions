class Solution(object):
    def removeInvalidParentheses(self, s):
        def is_valid(st):
            count = 0
            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        level = {s}
        while True:
            valid = [st for st in level if is_valid(st)]
            if valid:
                return list(set(valid))
            next_level = set()
            for st in level:
                for i in range(len(st)):
                    if st[i] in '()':
                        next_level.add(st[:i] + st[i+1:])
            level = next_level