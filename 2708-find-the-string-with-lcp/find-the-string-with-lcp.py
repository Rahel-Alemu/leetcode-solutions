class Solution:
    def findTheString(self, lcp):
        n = len(lcp)
        res = [""] * n
        curr = 0
        for i in range(n):
            if res[i] != "":
                continue
            if curr >= 26:
                return ""
            char = chr(ord('a') + curr)
            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = char
            curr += 1
        
        for char in res:
            if char == "":
                return ""
        
        s = "".join(res)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                val = 0
                if s[i] == s[j]:
                    val = (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0) + 1
                if lcp[i][j] != val:
                    return ""
        return s