class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                current = stack.pop()

                if current == 0:
                    score = 1
                else:
                    score = 2 * current

                stack[-1] += score

        return stack[0]