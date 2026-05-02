class Solution:
    def rotatedDigits(self, n):
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            if any(c in '347' for c in s):
                continue
            if any(c in '2569' for c in s):
                count += 1
        return count