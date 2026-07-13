class Solution(object):
    def sequentialDigits(self, low, high):
        s = "123456789"
        res = []
        for length in range(2, 10):
            for i in range(10 - length):
                num = int(s[i:i+length])
                if low <= num <= high:
                    res.append(num)
        return res