class Solution:
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1, s2):
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            self.memo[(s1, s2)] = False
            return False
            
        n = len(s1)
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
               (self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i])):
                self.memo[(s1, s2)] = True
                return True
                
        self.memo[(s1, s2)] = False
        return False