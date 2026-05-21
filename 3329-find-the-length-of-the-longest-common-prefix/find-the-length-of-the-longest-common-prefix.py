class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        prefixes = set()
        for x in arr1:
            s = str(x)
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])
                
        max_len = 0
        for y in arr2:
            s = str(y)
            for i in range(max_len + 1, len(s) + 1):
                if s[:i] in prefixes:
                    max_len = i
                else:
                    break
                    
        return max_len