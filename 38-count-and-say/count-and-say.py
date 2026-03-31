class Solution:
    def countAndSay(self, n):
        result = "1"

        for _ in range(n - 1):
            i = 0
            new_result = ""

            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                new_result += str(count) + result[i]
                i += 1

            result = new_result

        return result