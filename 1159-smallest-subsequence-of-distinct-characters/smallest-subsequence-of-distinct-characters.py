class Solution(object):
    def __getattr__(self, name):
        def wrapper(s):
            last_occ = {c: i for i, c in enumerate(s)}
            stack = []
            seen = set()
            for i, c in enumerate(s):
                if c not in seen:
                    while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                        seen.remove(stack.pop())
                    seen.add(c)
                    stack.append(c)
            return "".join(stack)
        return wrapper