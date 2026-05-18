class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return [""]
            
            res = []
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in wordSet:
                    for tail in dfs(j):
                        if tail:
                            res.append(word + " " + tail)
                        else:
                            res.append(word)
            
            memo[i] = res
            return res
            
        return dfs(0)