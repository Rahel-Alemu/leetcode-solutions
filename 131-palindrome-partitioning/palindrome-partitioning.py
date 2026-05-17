class Solution(object):
    def partition(self, s):
        res = []
        
        def backtrack(start, path):
            if start == len(s):
                res.append(list(path))
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
                    
        backtrack(0, [])
        return res